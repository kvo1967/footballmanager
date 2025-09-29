import requests
import json
from datetime import datetime, timezone, timedelta
import os
from clubs.club_registry import club_registry
from matches.match import Match


class OddsApiClient:
    """
    Get FDR (Fixture Difficulty Rating) via average odds of betting sites
    """
    def __init__(self, api_key_file="api-key.txt"):
        self.api_key = self._read_api_key(api_key_file)
        self.base_url = "https://api.the-odds-api.com/v4"

    def _read_api_key(self, api_key_file):
        """Read API key from file"""
        try:
            # If relative path, look from the project root directory
            if not os.path.isabs(api_key_file):
                # Get the project root (go up two levels from matches/odds_/)
                current_dir = os.path.dirname(os.path.abspath(__file__))
                project_root = os.path.dirname(os.path.dirname(current_dir))
                api_key_file = os.path.join(project_root, api_key_file)

            with open(api_key_file, 'r') as f:
                return f.read().strip()
        except FileNotFoundError:
            raise FileNotFoundError(f"API key file '{api_key_file}' not found")
        except Exception as e:
            raise Exception(f"Error reading API key: {e}")

    def _get_next_sunday(self):
        """Calculate the date of the next upcoming Sunday"""
        today = datetime.now()
        days_ahead = 6 - today.weekday()  # Sunday is 6, Monday is 0

        if days_ahead <= 0:  # Today is Sunday or later in the week
            days_ahead += 7

        next_sunday = today + timedelta(days=days_ahead)
        return next_sunday.strftime("%Y-%m-%d")

    def fetch_eredivisie_odds(self):
        """Fetch odds for Dutch Eredivisie matches"""
        url = f"{self.base_url}/sports/soccer_netherlands_eredivisie/odds"
        params = {
            'regions': 'eu',
            'oddsFormat': 'decimal',
            'apiKey': self.api_key
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching odds: {e}")
            return []

    def normalize_team_name(self, team_name):
        """Convert API team names to our club names"""
        # Mapping of API team names to our club registry names
        name_mappings = {
            'FC Twente Enschede': 'twente',
            'Fortuna Sittard': 'fortuna sittard',
            'Ajax Amsterdam': 'ajax',
            'AZ Alkmaar': 'az',
            'Feyenoord Rotterdam': 'feyenoord',
            'Go Ahead Eagles': 'go ahead eagles',
            'FC Groningen': 'fc groningen',
            'sc Heerenveen': 'heerenveen',
            'Heracles Almelo': 'heracles',
            'NAC Breda': 'nac breda',
            'NEC Nijmegen': 'nec',
            'PEC Zwolle': 'pec zwolle',
            'FC Zwolle': 'pec zwolle',  # Alternative name for PEC Zwolle
            'PSV Eindhoven': 'psv',
            'Excelsior Rotterdam': 'excelsior',
            'Sparta Rotterdam': 'sparta rotterdam',
            'FC Utrecht': 'fc utrecht',
            'FC Volendam': 'fc volendam',
            'Telstar': 'telstar',
            'SC Telstar': 'telstar'  # Alternative name for Telstar
        }

        normalized_name = name_mappings.get(team_name, team_name.lower())
        return club_registry.get_by_name(normalized_name)

    def average_odds(self, bookmakers, home_team_name, away_team_name):
        """Average odds across all bookmakers for a match"""
        home_odds = []
        draw_odds = []
        away_odds = []

        for bookmaker in bookmakers:
            for market in bookmaker.get('markets', []):
                if market.get('key') == 'h2h':
                    outcomes = market.get('outcomes', [])
                    for outcome in outcomes:
                        if outcome['name'] == 'Draw':
                            draw_odds.append(outcome['price'])
                        elif outcome['name'] == home_team_name:
                            home_odds.append(outcome['price'])
                        elif outcome['name'] == away_team_name:
                            away_odds.append(outcome['price'])

        # Calculate averages
        avg_home = sum(home_odds) / len(home_odds) if home_odds else 1.0
        avg_draw = sum(draw_odds) / len(draw_odds) if draw_odds else 1.0
        avg_away = sum(away_odds) / len(away_odds) if away_odds else 1.0

        return avg_home, avg_draw, avg_away

    def odds_to_percentages(self, home_odds, draw_odds, away_odds):
        """Convert decimal odds to implied probabilities (percentages)"""
        home_prob = (1 / home_odds) * 100 if home_odds > 0 else 0
        draw_prob = (1 / draw_odds) * 100 if draw_odds > 0 else 0
        away_prob = (1 / away_odds) * 100 if away_odds > 0 else 0

        # Normalize to sum to 100%
        total = home_prob + draw_prob + away_prob
        if total > 0:
            home_prob = (home_prob / total) * 100
            draw_prob = (draw_prob / total) * 100
            away_prob = (away_prob / total) * 100

        return round(home_prob, 1), round(draw_prob, 1), round(away_prob, 1)

    def get_weekend_matches(self, end_date=None):
        """Get matches for this weekend (up to next Sunday by default)"""
        if end_date is None:
            end_date = self._get_next_sunday()

        odds_data = self.fetch_eredivisie_odds()
        weekend_matches = []

        end_datetime = datetime.strptime(end_date + "T23:59:59Z", "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)

        for match_data in odds_data:
            match_time = datetime.fromisoformat(match_data['commence_time'].replace('Z', '+00:00'))

            if match_time <= end_datetime:
                home_team = self.normalize_team_name(match_data['home_team'])
                away_team = self.normalize_team_name(match_data['away_team'])

                if home_team and away_team:
                    match = Match(home_team, away_team)

                    # Calculate average odds
                    home_odds, draw_odds, away_odds = self.average_odds(
                        match_data['bookmakers'],
                        match_data['home_team'],
                        match_data['away_team']
                    )

                    # Convert to percentages
                    home_pct, draw_pct, away_pct = self.odds_to_percentages(home_odds, draw_odds, away_odds)

                    match.set_odds(home_pct, draw_pct, away_pct)
                    match.match_time = match_time
                    weekend_matches.append(match)

        return weekend_matches
from matches.odds_.odds_api_client import OddsApiClient
from datetime import datetime

def display_weekend_matches():
    # Initialize the API client (reads API key from api-key.txt)
    api_client = OddsApiClient()

    # Get weekend matches (automatically calculates next Sunday)
    matches = api_client.get_weekend_matches()

    # Get the end date for display
    end_date = api_client._get_next_sunday()
    end_date_formatted = datetime.strptime(end_date, "%Y-%m-%d").strftime("%B %d, %Y")

    print(f"WEEKEND MATCHES (up to {end_date_formatted})")
    print("=" * 100)

    if not matches:
        print("No matches found for this weekend.")
        return

    # Calculate column widths
    max_home_len = max(len(match.home_team.name) for match in matches) if matches else 15
    max_away_len = max(len(match.away_team.name) for match in matches) if matches else 15

    home_width = max(max_home_len, 12)
    away_width = max(max_away_len, 12)

    # Table headers
    print(f"{'Date/Time':<16} {'Home Team':<{home_width}} {'Away Team':<{away_width}} {'Home%':<6} {'Draw%':<6} {'Away%':<6}")
    print(f"{'-'*16} {'-'*home_width} {'-'*away_width} {'-'*6} {'-'*6} {'-'*6}")

    # Sort matches by date/time
    sorted_matches = sorted(matches, key=lambda x: x.match_time)

    for match in sorted_matches:
        match_datetime = match.match_time.strftime("%a %d %H:%M")
        print(f"{match_datetime:<16} {match.home_team.name:<{home_width}} {match.away_team.name:<{away_width}} {match.home_win:<6}% {match.draw:<6}% {match.away_win:<6}%")

    print(f"\nTotal matches this weekend: {len(matches)}")

if __name__ == "__main__":
    display_weekend_matches()
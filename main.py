from players.import_.import_players import get_players_from_fantasy_game
from players.import_.import_unavailable import get_unavailable_players
from players.matching import get_available_players
from players.log_.player_writer import write_players_to_file
from players.log_.available_writer import write_available_to_file
from players.log_.unavailable_writer import write_unavailable_to_file
from players.log_.error_writer import write_errors_to_file
from matches.odds_.odds_api_client import OddsApiClient
from matches.match_writer import write_weekend_matches_to_file
from datetime import datetime

def get_budget_from_user():
    """
    Ask user for total budget amount via command line input.

    Returns:130
        int: Budget amount in millions of euros
    """
    while True:
        try:
            budget = float(input("Enter your total budget in millions of euros (e.g., 115): "))
            if budget > 0:
                return int(budget)
            else:
                print("Budget must be a positive number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def create_final_prompt(budget, weekend_matches, available_players):
    """
    Create the final LLM prompt by combining budget, matches, and player data.

    Args:
        budget: Total budget in millions of euros
        weekend_matches: List of weekend matches with odds
        available_players: List of available players for selection

    Returns:
        str: Complete prompt content for the LLM
    """
    # Read the basic prompt template
    with open('docs/basic_prompt.md', 'r', encoding='utf-8') as f:
        prompt_content = f.read()

    # Replace budget placeholder
    prompt_content = prompt_content.replace('[XXX]', str(budget))

    # Add weekend matches section (replace the static example)
    matches_text = "## Wedstrijdschema met winstkansen\n"
    matches_text += "Date/Time        Home Team       Away Team        Home%  Draw%  Away%\n"
    matches_text += "---------------- --------------- ---------------- ------ ------ ------\n"

    sorted_matches = sorted(weekend_matches, key=lambda x: x.match_time)
    for match in sorted_matches:
        match_datetime = match.match_time.strftime("%a %d %H:%M")
        matches_text += f"{match_datetime:<16} {match.home_team.name:<15} {match.away_team.name:<16} {match.home_win:<6}% {match.draw:<6}% {match.away_win:<6}%\n"

    # Replace the static matches section
    import re
    pattern = r'## Wedstrijdschema met winstkansen.*?(?=\n## )'
    prompt_content = re.sub(pattern, matches_text, prompt_content, flags=re.DOTALL)

    # Add available players section at the end
    players_text = "\n\n## Beschikbare Spelers\n\n"
    players_text += "Club\tSpeler\tPositie\tPrijs\tScore\n"
    players_text += "----\t------\t-------\t-----\t-----\n"

    # Sort players by club and name for better readability
    sorted_players = sorted(available_players, key=lambda x: (x.club.name, x.name))
    for player in sorted_players:
        players_text += f"{player.club.name}\t{player.name}\t{player.position}\t€{player.price}M\t{player.score}\n"

    prompt_content += players_text

    return prompt_content

def display_summary_statistics(players_list, unavailable_list, available_list, error_list, weekend_matches):
    """
    Display summary statistics of the football data collection process.

    Shows counts for all collected data types and indicates where files are written.
    Provides clear feedback on data processing success and any matching issues.

    Args:
        players_list: List of all players from fantasy football game
        unavailable_list: List of injured/suspended players
        available_list: List of players ready to play
        error_list: List of matching errors between data sources
        weekend_matches: List of weekend matches with odds data
    """
    # Display count of each data collection category
    print(f"All players: {len(players_list)} (written to all_players.txt)")
    print(f"Unavailable players: {len(unavailable_list)} (written to unavailable_players.txt)")
    print(f"Available players: {len(available_list)} (written to available_players.txt)")
    print(f"Weekend matches: {len(weekend_matches)} (written to weekend_matches.txt)")

    # Show matching errors if any occurred during name matching process
    if error_list:
        print(f"Matching errors: {len(error_list)} (written to matching_errors.txt)")
    else:
        print("No matching errors found!")

def display_weekend_matches(matches, end_date):
    """
    Display weekend football matches in a formatted table with odds information.

    Shows match details including date/time, team names, and win probabilities.
    Automatically calculates optimal column widths based on team name lengths.

    Args:
        matches: List of Match objects containing team info and odds
        end_date: String date in YYYY-MM-DD format for display purposes
    """
    # Convert date string to readable format for header
    end_date_formatted = datetime.strptime(end_date, "%Y-%m-%d").strftime("%B %d, %Y")

    print(f"\nWEEKEND MATCHES (up to {end_date_formatted})")
    print("=" * 100)

    if not matches:
        print("No matches found for this weekend.")
        return

    # Calculate optimal column widths based on team name lengths
    max_home_len = max(len(match.home_team.name) for match in matches) if matches else 15
    max_away_len = max(len(match.away_team.name) for match in matches) if matches else 15

    # Ensure minimum width for readability
    home_width = max(max_home_len, 12)
    away_width = max(max_away_len, 12)

    # Print table headers with dynamic column widths
    print(f"{'Date/Time':<16} {'Home Team':<{home_width}} {'Away Team':<{away_width}} {'Home%':<6} {'Draw%':<6} {'Away%':<6}")
    print(f"{'-'*16} {'-'*home_width} {'-'*away_width} {'-'*6} {'-'*6} {'-'*6}")

    # Sort matches chronologically for logical presentation
    sorted_matches = sorted(matches, key=lambda x: x.match_time)

    # Display each match with formatted date and odds percentages
    for match in sorted_matches:
        match_datetime = match.match_time.strftime("%a %d %H:%M")
        print(f"{match_datetime:<16} {match.home_team.name:<{home_width}} {match.away_team.name:<{away_width}} {match.home_win:<6}% {match.draw:<6}% {match.away_win:<6}%")

    print(f"\nTotal matches this weekend: {len(matches)}")


# Main execution: Collect all football data and generate reports
# ============================================================

# 1. Collect player data from fantasy football website and injury reports
players_list = get_players_from_fantasy_game()
unavailable_list = get_unavailable_players()
available_list, error_list = get_available_players(players_list, unavailable_list)

# 2. Fetch weekend match odds from API
api_client = OddsApiClient()
weekend_matches = api_client.get_weekend_matches()
end_date = api_client._get_next_sunday()

# 3. Generate output files for analysis
write_players_to_file(players_list, "all_players.txt")
write_unavailable_to_file(unavailable_list, "unavailable_players.txt")
write_available_to_file(available_list, "available_players.txt")
write_errors_to_file(error_list, "matching_errors.txt")
write_weekend_matches_to_file(weekend_matches, "weekend_matches.txt")

# 4. Display summary statistics
display_summary_statistics(players_list, unavailable_list, available_list, error_list, weekend_matches)

# 5. Show weekend matches with odds
display_weekend_matches(weekend_matches, end_date)

# 6. Get budget from user and create final LLM prompt
budget = get_budget_from_user()
final_prompt = create_final_prompt(budget, weekend_matches, available_list)

# 7. Write final prompt to file
with open("final_prompt.md", "w", encoding="utf-8") as f:
    f.write(final_prompt)

print(f"\nFinal LLM prompt created with budget of €{budget}M (written to final_prompt.md)")

from datetime import datetime

def write_weekend_matches_to_file(matches, filename):
    """Write weekend matches with odds to file (tab-separated)"""
    # Sort matches chronologically for logical presentation
    sorted_matches = sorted(matches, key=lambda x: x.match_time)

    with open(filename, 'w', encoding='utf-8') as f:
        # Write header
        f.write(f"Date/Time\tHome Team\tAway Team\tHome%\tDraw%\tAway%\n")

        # Write each match with formatted date and odds percentages
        for match in sorted_matches:
            match_datetime = match.match_time.strftime("%a %d %H:%M")
            f.write(f"{match_datetime}\t{match.home_team.name}\t{match.away_team.name}\t{match.home_win}%\t{match.draw}%\t{match.away_win}%\n")
def get_available_players(players_list, unavailable_list):
    """
    Calculate available players by removing unavailable (injured/suspended) players from the full roster.

    Uses intelligent name matching to handle different name formats:
    - Fantasy game format: "Family, Initials" (e.g., "van Dijk, V")
    - Unavailable list format: "Given Family" (e.g., "Virgil van Dijk")

    Args:
        players_list: List of all players from fantasy football game
        unavailable_list: List of injured/suspended players

    Returns:
        tuple: (available_players, error_list)
            - available_players: Players ready to play (not unavailable)
            - error_list: Players that couldn't be matched between the two lists
    """
    matched_players = set()  # Players confirmed as unavailable
    error_list = []          # Unmatched players for debugging

    # For each unavailable player, find their match in the full players list
    for unavailable in unavailable_list:
        matches = []

        # First filter by club - only check players from the same team
        club_players = [p for p in players_list if p.club == unavailable.club]

        # Then try to match names using intelligent Dutch name parsing
        for player in club_players:
            if player.matches_unavailable_name(unavailable.player_name):
                matches.append(player)

        # Validate matching results
        if len(matches) == 1:
            # Perfect match - mark player as unavailable
            matched_players.add(matches[0])
        elif len(matches) == 0:
            # No match found - potential data issue
            error_list.append(f"No match found for {unavailable.player_name} ({unavailable.club.name})")
        else:
            # Multiple matches - ambiguous, needs investigation
            error_list.append(f"Multiple matches found for {unavailable.player_name} ({unavailable.club.name}): {[p.name for p in matches]}")

    # Available players = all players minus the unavailable ones
    available_players = [p for p in players_list if p not in matched_players]

    return available_players, error_list
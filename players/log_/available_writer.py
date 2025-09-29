def write_available_to_file(available_list, filename):
    """Write available players list to file with club headers and fixed-width columns"""

    def position_sort_key(position):
        """Convert position to sort order: K, V, M, A"""
        position_order = {'K': 0, 'V': 1, 'M': 2, 'A': 3}
        return position_order.get(position, 999)  # Unknown positions go to end

    def sort_key(player):
        """Sort by club, then position order, then score desc, then price desc"""
        return (
            player.club.name,
            position_sort_key(player.position),
            -int(player.score) if str(player.score).isdigit() else 0,
            -float(player.price) if str(player.price).replace('.', '').isdigit() else 0
        )

    sorted_list = sorted(available_list, key=sort_key)

    if not sorted_list:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("No available players found.\n")
        return

    # Calculate maximum widths for each column
    max_name_width = max(len(player.name) for player in sorted_list)
    max_position_width = max(len(player.position) for player in sorted_list)
    max_price_width = max(len(str(player.price)) for player in sorted_list)
    max_score_width = max(len(str(player.score)) for player in sorted_list)

    # Set minimum widths for headers
    name_width = max(max_name_width, len("Player"))
    position_width = max(max_position_width, len("Position"))
    price_width = max(max_price_width, len("Price"))
    score_width = max(max_score_width, len("Score"))

    with open(filename, 'w', encoding='utf-8') as f:
        f.write("AVAILABLE PLAYERS\n")
        f.write("=" * 80 + "\n\n")

        current_club = None
        for player in sorted_list:
            # Write club header when club changes
            if current_club != player.club.name:
                if current_club is not None:  # Add spacing between clubs
                    f.write("\n")

                current_club = player.club.name
                f.write(f"{current_club.upper()}\n")
                f.write("-" * 60 + "\n")

                # Write column headers
                f.write(f"{'Player':<{name_width}} {'Position':<{position_width}} {'Price':<{price_width}} {'Score':<{score_width}}\n")
                f.write(f"{'-' * name_width} {'-' * position_width} {'-' * price_width} {'-' * score_width}\n")

            # Write player data
            f.write(f"{player.name:<{name_width}} {player.position:<{position_width}} {player.price:<{price_width}} {player.score:<{score_width}}\n")

        f.write(f"\nTotal available players: {len(sorted_list)}\n")
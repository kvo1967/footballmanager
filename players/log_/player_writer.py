def write_players_to_file(players_list, filename):
    """Write complete player list with all stats to file (tab-separated)"""
    sorted_list = sorted(players_list, key=lambda x: (x.club.name, x.name))

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Club\tPlayer\tPosition\tPrice\tPlayed\tWon\tDraw\tLost\tGoals For\tGoals Against\tClean Sheet\tAssist\tYellow\tRed\tOG\tScore\n")
        for player in sorted_list:
            f.write(f"{player.club.name}\t{player.name}\t{player.position}\t{player.price}\t{player.played}\t{player.won}\t{player.draw}\t{player.lost}\t{player.goals_for}\t{player.goals_against}\t{player.clean_sheet}\t{player.assist}\t{player.yellow}\t{player.red}\t{player.og}\t{player.score}\n")
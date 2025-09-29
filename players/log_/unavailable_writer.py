def write_unavailable_to_file(unavailable_list, filename):
    """Write unavailable players list to file (tab-separated)"""
    sorted_list = sorted(unavailable_list, key=lambda x: x.club.name)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Club\tPlayer\tReason\tExpected Return\n")
        for unavailable in sorted_list:
            f.write(f"{unavailable.club.name}\t{unavailable.player_name}\t{unavailable.description}\t{unavailable.expected_return}\n")
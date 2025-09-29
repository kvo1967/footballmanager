def write_errors_to_file(error_list, filename):
    """Write matching errors to file"""
    if error_list:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("Matching Errors:\n")
            f.write("=" * 50 + "\n")
            for error in error_list:
                f.write(f"• {error}\n")
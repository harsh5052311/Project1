# landing_page.py

def print_landing_page():
    # ANSI escape codes for colors
    RESET = "\033[0m"
    BOLD = "\033[1m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"

    # Clear screen
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    # Header
    print(BOLD + BLUE + "=" * 50 + RESET)
    print(BOLD + GREEN + "           WELCOME TO MY LANDING PAGE           " + RESET)
    print(BOLD + BLUE + "=" * 50 + RESET)
    print("")

    # Navigation
    print(CYAN + "   [ Home ]   [ About ]   [ Services ]   [ Contact ]" + RESET)
    print("")
    print(YELLOW + "-" * 50 + RESET)

    # Body content
    print(GREEN + "   This is a basic Python landing page demo." + RESET)
    print("   You can customize this text to showcase")
    print("   your project, portfolio, or business.")
    print(YELLOW + "-" * 50 + RESET)
    print("")

    # Content boxes
    box = [
        "***************   ***************",
        "*             *   *             *",
        "*   CONTENT   *   *   CONTENT   *",
        "*             *   *             *",
        "***************   ***************"
    ]
    for line in box:
        print(BOLD + CYAN + line + RESET)

    print("")
    # Footer
    print(BOLD + BLUE + "=" * 50 + RESET)
    print(BOLD + GREEN + "           Thank you for visiting!              " + RESET)
    print(BOLD + BLUE + "=" * 50 + RESET)


if __name__ == "__main__":
    print_landing_page()


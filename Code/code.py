"""
ASCII Art Smiley Face Generator

This program prints a smiley face using ASCII art when run.
Each function and variable is documented for clarity.
"""

def generate_smiley_art():
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]

    """
    return (
        "   *****   \n"
        "  *     *  \n"
        " *  o o  * \n"
        " *   ^   * \n"
        "  * \___/ * \n"
        "   *****   "
    )

def print_intro():
    """
    Prints an introduction message for the program.
    """
    print("Welcome to the ASCII Art Smiley Face Generator!")

def display_smiley(smiley_art):
    """
    Displays the ASCII art smiley face.

    Args:
        smiley_art (str): The ASCII art of the smiley face to display.
    """
    print(smiley_art)

def run_program():
    """
    Coordinates the execution of the program.
    """
    print_intro()
    smiley_art = generate_smiley_art()
    display_smiley(smiley_art)

if __name__ == "__main__":
    """
    Entry point of the program.

    Calls the `run_program` function to start the program.
    """
    run_program()

"""
ASCII Art Smiley Face Generator

This program prints a smiley face using ASCII art when run.
Each function and variable is documented for clarity.
"""

def print_smiley():
    """
    Prints an ASCII art smiley face to the console.

    The ASCII art uses a combination of special characters to depict a smiling face.
    """
    smiley_art = (
        "   *****   \n"
        "  *     *  \n"
        " *  o o  * \n"
        " *   ^   * \n"
        "  * \___/ * \n"
        "   *****   "
    )

    # Print the ASCII art to the console
    print(smiley_art)

if __name__ == "__main__":
    """
    Entry point of the program.

    Calls the `print_smiley` function to display the smiley face.
    """
    print_smiley()
import string


def clean_line(line: str) -> str:
    """Cleans a string from punctuations chars, makes all chars lowercase and removes redundant spaces.

    Args:
        line (str): string to clean.

    Returns:
        str: cleaned string
    """
    line = line.lower()                                                 # all lower case letters
    line = ' '.join(line.split())                                       # keeps only one space between words
    return line.translate(str.maketrans('', '', string.punctuation))    # removes punctuation 

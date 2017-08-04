alpha = 'abcdefghijklmnopqrstuvwxyz'

def is_pangram(text):
    """Function which checks if a string contains all the letters of an alphabet at least once

     Args:
         str: Text to be checked.

     Returns:
         bool: if the text contains all alphabets at least once
     """
    return (all(x in list(set(text.lower())) for x in list(alpha)))
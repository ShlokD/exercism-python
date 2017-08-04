def is_isogram(phrase):
    """Function which checks if a sentence does not contain any repeating letters

        Args:
            str: A phrase to be checked.

        Returns:
            bool: True if the phrase is an isogram, false otherwise
        """
    cleanphrase = phrase.replace(" ", "").replace("-", "").lower()
    return len(set(cleanphrase)) == len(cleanphrase)

def is_leap_year(year):
    """Function which checks if a year is a leap year.

    Args:
        int: year.

    Returns:
        bool: True if the year is a leap year, False otherwise
    """

    return year % 400 == 0 or (year %4 == 0 and year % 100 != 0)

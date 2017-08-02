def is_leap_year(year):
    """Function which checks if a year is a leap yeasr.

    Args:
        int: year.

    Returns:
        bool: if the year is a leap year
    """

    return year % 400 == 0 or (year %4 == 0 and year % 100 != 0)

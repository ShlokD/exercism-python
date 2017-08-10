import datetime

def add_gigasecond(day):
    giga = 10 ** 9
    return day + datetime.timedelta(seconds=giga)
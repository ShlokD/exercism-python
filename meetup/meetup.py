import datetime, math

def teenth_day(day):
    return 13 <= day.day and day.day <= 19

def nth_day(n):
    def is_nth_day(day):
        return math.floor((day.day - 1) / 7) == n-1
    return is_nth_day

def last_day(day):
    return day.month != (day + datetime.timedelta(days=7)).month

meetup_rules_to_func_map = {'1st': nth_day(1),'2nd': nth_day(2),
'3rd': nth_day(3),'4th': nth_day(4),
'5th': nth_day(5),'teenth': teenth_day,
'last': last_day
}

def meetup_day(year, month, weekday, meetup_rule):
    day = datetime.date(year, month, 1)
    # Tests everyday in the month until the weekday and condition are met
    while day.month == month:
        if day.weekday() == days_of_week[weekday] and meetup_rules_to_func_map[meetup_rule](day):
            return day
        day += datetime.timedelta(days=1)
    raise AssertionError("Not a valid meetup day")

days_of_week = {
'Monday'   : 0, 'Tuesday'  : 1,
'Wednesday': 2,  'Thursday' : 3,
'Friday'   : 4, 'Saturday' : 5,
'Sunday'   : 6}


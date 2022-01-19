from datetime import date, timedelta
from enum import Enum


class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

    def days_until(self, weekday):
        if self.value <= weekday.value:
            return weekday.value - self.value

        return weekday.value + 7 - self.value


class NextDate:

    def __init__(self, weekday: Weekday, after_today=False):
        self.weekday = weekday
        self.after_today = after_today

    def days_until(self):
        _days_until = Weekday(date.today().weekday()).days_until(self.weekday)
        if _days_until == 0 and self.after_today:
            return 7
        return _days_until

    def date(self):
        return date.today() + timedelta(days=self.days_until())

    def __repr__(self):
        return f"NextDate(Weekday.{self.weekday.name}, after_today={self.after_today})"


next_monday = NextDate(Weekday.MONDAY)
print(next_monday.days_until())
print(next_monday.date())
print(NextDate(Weekday.MONDAY), '\n')

next_monday = NextDate(Weekday.FRIDAY)
print(next_monday.days_until())
print(next_monday.date(), '\n')

next_monday = NextDate(Weekday.FRIDAY, after_today=True)
print(next_monday.days_until())
print(next_monday.date(), '\n')


# bonus 3 - same with functions
def days_until(weekday: Weekday, after_today=False):
    _days_until = Weekday(date.today().weekday()).days_until(weekday)
    if _days_until == 0 and after_today:
        return 7
    return _days_until


def next_date(weekday: Weekday, after_today=False):
    return date.today() + timedelta(days=days_until(weekday, after_today))


from functools import partial

next_tuesday = partial(next_date, weekday=Weekday.TUESDAY)
days_to_tuesday = partial(days_until, weekday=Weekday.TUESDAY)

print(next_tuesday(after_today=True))

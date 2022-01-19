def get_earliest(date1: str, date2: str):
    (month1, day1, year1) = date1.split('/')
    (month2, day2, year2) = date2.split('/')

    if (year1, month1, day1) < (year2, month2, day2):
        return date1
    else:
        return date2


print(get_earliest("01/27/1832", "01/27/1756"))
print(get_earliest("02/29/1972", "12/21/1946"))
print(get_earliest("02/24/1946", "03/21/1946"))
print(get_earliest("06/21/1958", "06/24/1958"))


def get_earliest(*dates):
    def normalize(date):
        (month, day, year) = date.split('/')
        return year, month, day

    return min(dates, key=normalize)

print(get_earliest("02/24/1946", "01/29/1946", "03/29/1945"))

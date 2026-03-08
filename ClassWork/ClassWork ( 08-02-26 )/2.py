def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(year, month):
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap(year) else 28
    else:
        return 31


def date_to_absolute_date(day, month, year):
    total_days = day

    for y in range(1, year):
        total_days += 366 if is_leap(y) else 365

    for m in range(1, month):
        total_days += days_in_month(year, m)

    return total_days


def days_diff(day1, month1, year1, day2, month2, year2):

    abs_date1 = date_to_absolute_date(day1, month1, year1)
    abs_date2 = date_to_absolute_date(day2, month2, year2)

    return abs(abs_date1 - abs_date2)


result = days_diff(1, 1, 2026, 8, 3, 2026)
print(f'Разница: {result}')
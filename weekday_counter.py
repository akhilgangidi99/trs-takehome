import argparse

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(month, year):
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 31

def days_until_date(day, month, year):
    days = day + 365 * (year - 1) + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400
    month_days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
    days += month_days[month - 1]
    if month > 2 and is_leap_year(year):
        days += 1
    return days

def zellers_congruence(day, month, year):
    if month < 3:
        month += 12
        year -= 1
    K = year % 100
    J = year // 100
    f = day + ((13 * (month + 1)) // 5) + K + (K // 4) + (J // 4) - (2 * J)
    return (f % 7 + 7) % 7

def count_weekdays(start_date, end_date):
    start_month, start_day, start_year = map(int, start_date.split('-'))
    end_month, end_day, end_year = map(int, end_date.split('-'))

    days_start = days_until_date(start_day, start_month, start_year)
    days_end = days_until_date(end_day, end_month, end_year)

    total_days = days_end - days_start + 1
    full_weeks = total_days // 7
    weekdays = full_weeks * 5

    remaining_days = total_days % 7
    start_weekday = zellers_congruence(start_day, start_month, start_year)

    for i in range(remaining_days):
        if start_weekday > 1:
            weekdays += 1
        start_weekday = (start_weekday + 1) % 7

    return weekdays

def main():
    parser = argparse.ArgumentParser(description='Weekday count between two dates')
    parser.add_argument("start_date", type=str, help='Enter a start date in MM-DD-YYYY format')
    parser.add_argument("end_date", type=str, help='Enter an end date in MM-DD-YYYY format')

    args = parser.parse_args()
    start_date = args.start_date
    end_date = args.end_date

    try:
        weekdays = count_weekdays(start_date, end_date)
        print(f"Number of weekdays between {start_date} and {end_date}: {weekdays}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
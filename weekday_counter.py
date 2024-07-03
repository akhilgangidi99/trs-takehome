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

def zellers_congruence(day, month, year):
    if month < 3:
        month += 12
        year -= 1
    K = year % 100
    J = year // 100
    f = day + ((13 * (month + 1)) // 5) + K + (K // 4) + (J // 4) - (2 * J)
    return (f % 7 + 7) % 7

def is_weekday(day, month, year):
    day_of_week = zellers_congruence(day, month, year)
    return day_of_week not in [0, 1]

def increment_date(day, month, year):
    day += 1
    if day > days_in_month(month, year):
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    return day, month, year

def count_weekdays(start_date, end_date):
    start_month, start_day, start_year = map(int, start_date.split('-'))
    end_month, end_day, end_year = map(int, end_date.split('-'))

    weekday_count = 0
    current_month, current_day, current_year = start_month, start_day, start_year

    while (current_year, current_month, current_day) <= (end_year, end_month, end_day):
        if is_weekday(current_day, current_month, current_year):
            weekday_count += 1
        current_day, current_month, current_year = increment_date(current_day, current_month, current_year)

    return weekday_count

def main():
    parser = argparse.ArgumentParser(description='Weekday count between two dates')
    parser.add_argument("start_date", type=str, help='Enter a start date in MM-DD-YYYY format')
    parser.add_argument("end_date", type=str, help='Enter a end date in MM-DD-YYYY format')

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
import argparse 
from datetime import datetime, timedelta

def weekday_counter(start_date, end_date):
    try:
        start_date = datetime.strptime(start_date, '%m-%d-%Y')
        end_date = datetime.strptime(end_date, '%m-%d-%Y')
    except ValueError:
        raise ValueError("Dates must be in MM-DD-YYYY format")

    total_days = (end_date - start_date).days + 1
    full_weeks = total_days // 7

    weekday_count = full_weeks * 5

    remaining_days = total_days % 7
    
    for i in range(remaining_days):
        current_day = start_date + timedelta(days=full_weeks * 7 + i)
        if current_day.weekday() < 5:
            weekday_count += 1
    
    return weekday_count

def main():
    parser = argparse.ArgumentParser(description='Weekday count between two dates')
    parser.add_argument("start_date", type=str, help='Enter a start date in MM-DD-YYYY format')
    parser.add_argument("end_date", type=str, help='Enter a end date in MM-DD-YYYY format')

    args = parser.parse_args()
    start_date = args.start_date
    end_date = args.end_date

    try:
        weekdays = weekday_counter(start_date, end_date)
        print(f"Number of weekdays between {start_date} and {end_date}: {weekdays}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
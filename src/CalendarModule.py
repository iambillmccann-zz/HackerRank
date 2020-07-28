# Enter your code here. Read input from STDIN. Print output to STDOUT
from datetime import date
import calendar

if __name__ == "__main__":
    dates = list(map(int, input().strip().split()))
    my_date = date(dates[2], dates[0], dates[1])
    print(calendar.day_name[my_date.weekday()].upper())
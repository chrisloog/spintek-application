import csv
import datetime


def get_reminder_date(year, month, day, holidays):
    reminder_date = datetime.date(year, month, day)
    workdays = 0
    while workdays < 3:
        reminder_date -= datetime.timedelta(days=1)
        if reminder_date.weekday() < 5 and reminder_date not in holidays:
            workdays += 1
    return reminder_date


def is_valid_pay_day(pay_date, holidays):
    return pay_date.weekday() not in {5, 6} and pay_date not in holidays


def write_pay_schedule(year, holidays):
    with open(f"{year}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Month", "Pay Day", "Reminder Day"])
        for month in range(1, 13):
            pay_day = datetime.date(year, month, 10)
            while not is_valid_pay_day(pay_day, holidays):
                pay_day -= datetime.timedelta(days=1)
            reminder_day = get_reminder_date(year, month, pay_day.day, holidays).strftime("%Y-%m-%d")
            pay_day = pay_day.strftime("%Y-%m-%d")
            writer.writerow([month, pay_day, reminder_day])


if __name__ == "__main__":
    year = int(input("Enter the year: "))
    holidays = {
        datetime.date(year, 1, 1),
        datetime.date(year, 2, 24),
        datetime.date(year, 5, 1),
        datetime.date(year, 6, 23),
        datetime.date(year, 6, 24),
        datetime.date(year, 8, 20),
        datetime.date(year, 12, 24),
        datetime.date(year, 12, 25),
        datetime.date(year, 12, 26),
    }
    write_pay_schedule(year, holidays)

import datetime as dt

now = dt.datetime.now()
present_year = now.year
present_month = now.month
present_day = now.day
print(f"{present_year}-{present_month}-{present_day}")

present_date_format = now.date()
print(present_date_format)

date_of_birth = dt.datetime(year=2000, month=12, day=22, hour=1, minute=50, second=30)
print(date_of_birth)
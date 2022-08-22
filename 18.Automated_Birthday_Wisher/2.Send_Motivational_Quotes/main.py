import datetime as dt
import random
import smtplib

my_email = "tejendraofficial4@gmail.com"
my_password = "bkmqmyqszmzghhor"

present_date = dt.datetime.now()
present_week_day = present_date.weekday()
if present_week_day == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()  # stores as a list.
        monday_quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="tejendrayerra2000.4@gmail.com",
                            msg=f"Subject:Monday Quotes\n\n{monday_quote}.")
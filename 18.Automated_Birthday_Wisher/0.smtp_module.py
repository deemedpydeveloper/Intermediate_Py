import smtplib

my_email = "tejendraofficial4@gmail.com"
my_password = "bkmqmyqszmzghhor"  # generate app password in your google account.

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="yerraakhil451@gmail.com",
                        msg="Subject:Hacked!\n\nThis is my first hack.")
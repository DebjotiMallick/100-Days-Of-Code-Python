import smtplib
import datetime as dt
import random, os
from dotenv import load_dotenv

load_dotenv()

my_email = "debjoti97@gmail.com"
password = os.getenv('APP_PASSWORD')

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password) # type: ignore
        connection.sendmail(from_addr=my_email, to_addrs="debjoti.mallick@hotmail.com", msg=f"Subject:Monday Motivation\n\n{quote}")
        connection.close()


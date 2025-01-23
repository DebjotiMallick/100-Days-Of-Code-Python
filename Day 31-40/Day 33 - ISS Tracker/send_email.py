import smtplib, os
from dotenv import load_dotenv

load_dotenv()

my_email = "debjoti97@gmail.com"
password = os.getenv('APP_PASSWORD')

def send_email(subject,message):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password) #type: ignore
            connection.sendmail(from_addr=my_email, to_addrs="debjoti.mallick@hotmail.com", msg=f"Subject:{subject}\n\n{message}")
            connection.close()
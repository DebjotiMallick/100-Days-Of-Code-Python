import requests
import datetime as dt
import send_email

time_now = dt.datetime.now()
print(time_now)

MY_LAT = 22.572645
MY_LONG = 88.363892

def is_night():     
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "Asia/Kolkata"
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    if time_now.hour >= sunrise and time_now.hour <= sunset:
        return False
    else:
        return True

def is_iss_overhead():  
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])


    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LONG - 5 <= longitude <= MY_LONG + 5:
        return True
    else:
        return False

if is_night() and is_iss_overhead():
    send_email.send_email("ISS Overhead Mail","Look up")
else:
    send_email.send_email("ISS Overhead Mail","Don't look up")

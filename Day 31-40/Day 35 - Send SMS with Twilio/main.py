import requests
from pprint import pprint
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

apikey = os.getenv('APIKEY')
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

client = Client(account_sid, auth_token)

weather_params = {
    "q": "Brighton,GB",
    "appid": apikey,
    "units": "metric",
    "cnt": 4
}

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
will_rain = False

for hour_data in weather_data["list"]:
    if int(hour_data["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
    message = client.messages.create(
        body="It's going to rain today. Bring an umbrella",
        from_="+12316802776",
        to="+918017894299",
    )
    print(message.status)
else:
    print("No need for an umbrella")
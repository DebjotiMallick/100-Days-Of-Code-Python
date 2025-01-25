from dotenv import load_dotenv
import os, requests
from pprint import pprint
from datetime import datetime

load_dotenv()

GENDER = "male"
WEIGHT_KG = 66
HEIGHT_CM = 175
AGE = 27

url = "https://trackapi.nutritionix.com/v2/natural/exercise"
appid=os.getenv('NUTRITIONIX_APPID')
apikey=os.getenv('NUTRITIONIX_APIKEY')
token=os.getenv('SHEETY_TOKEN')

sheety_url = "https://api.sheety.co/fcdb578b7cf43e99873e65627e33b8bf/copyOfMyWorkouts/workouts"

exercises = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": appid,
    "x-app-key": apikey
}

parameters = {
    "query": exercises,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url, headers=headers, data=parameters)
result = response.json()

if token:
    sheety_headers = {"Authorization": "Bearer " + token}
else:
    raise ValueError("Sheety token is not set in the environment variables.")

for exercise in result["exercises"]:
    sheety_body = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    
    sheety_response = requests.post(sheety_url, headers=sheety_headers ,json=sheety_body)
    sheety_result = sheety_response.json()
    print(sheety_result)
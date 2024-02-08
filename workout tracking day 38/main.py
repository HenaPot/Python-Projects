import requests
from datetime import datetime


APP_ID = "appid"
API_KEY = "imakey!"
SHEETY_TOKEN = "secrettoken"

users_input = input("What kind of workout did you do today? ")

json_parametres = {
    "query": users_input,
    "gender": "female",
    "weight_kg": 56.5,
    "height_cm": 165.64,
    "age": 20
}

headers0 = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    # "Content-Type": "application/json"
}

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response0 = requests.post(url=nutritionix_endpoint, json=json_parametres, headers=headers0)
dictionary = response0.json()

sheety_api = "https://api.sheety.co/a6c2b664c897e7fc4d8ea48a15788c0a/workoutTracking/workouts"

headers1 = {
 "Authorization": "Bearer PUT_TOKEN_HERE"
}

today = datetime.now()
the_date = today.strftime("%d/%m/%Y")
the_time = today.strftime("%H:%M:%S")

# only works for 2 entries for some reason
activities_num = len(dictionary["exercises"])

for activity_num in range(activities_num):
    workout_json = {
     "workout": {
                "date": the_date,
                "time": the_time,
                "exercise": dictionary["exercises"][activity_num]["name"].title(),
                "duration": f"{dictionary['exercises'][activity_num]['duration_min']}",
                "calories": dictionary["exercises"][activity_num]["nf_calories"]
                }
    }
    response1 = requests.post(url=sheety_api, json=workout_json, headers=headers1)


# envioronment variables are causing some errors. namely, once i start using them, curiously, first API call thats
# barely using any of them (only API_KEY and APP_ID) gives error response and it crashes from then on


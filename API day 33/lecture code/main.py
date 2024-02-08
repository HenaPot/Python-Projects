import requests
from datetime import datetime

LATITUDE = 43.847057
LONGITUDE = -341.630774

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)

parametres = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": 0
}

time_now = datetime.utcnow().hour
print(time_now)

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parametres)
response.raise_for_status()

sunrise = response.json()["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = response.json()["results"]["sunset"].split("T")[1].split(":")[0]

# print(sunrise, sunset)
print(sunrise)
print(sunset)
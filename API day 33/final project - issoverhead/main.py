import requests
from datetime import datetime
import smtplib
import time


MY_LAT = 43  # Your latitude
MY_LONG = -341  # Your longitude
MY_EMAIL = "secretemail@gmail.com"
MY_PASSWORD = "secretpassword1"
RECIPIENT = "recipient@yahoo.com"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
iss_position = (iss_latitude, iss_longitude)


# Your position is within +5 or -5 degrees of the ISS position.
bigger_lat = MY_LAT + 5
smaller_lat = MY_LAT - 5
bigger_lng = MY_LONG + 5
smaller_lng = MY_LONG - 5

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.utcnow().hour


def is_dark():
    if time_now >= sunset:
        return True
    elif time_now <= sunrise:
        return True
    else:
        return False


while True:
    time.sleep(60)
    # If the ISS is close to my current position
    if smaller_lat <= iss_latitude <= bigger_lat:
        if smaller_lng <= iss_longitude <= bigger_lng:
            # and it is currentnow()ly dark
            if is_dark():
                # Then send me an email to tell me to look up.
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                    connection.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs=RECIPIENT,
                        msg="Subject:SATELITE ABOVE YOU\n\nLOOK UP,\n\n ISS isoverhead! "
                            "You programmed code to send you an email when this satelite is above your location."
                    )

# BONUS: run the code every 60 seconds.
# attempted using www.pythonanywhere.com --> NOT WORKING, ONLY FOR DAILY TASKS
# completed using time.sleep()

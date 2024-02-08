import requests
import smtplib

my_email = "testtest@gmail.com"
password = "passpasspass"

MY_LAT = 43
MY_LONG = 18
api_key = "generickeyyyy"
# another_one = "testpass"

# current weather
api_endpoint = "https://api.openweathermap.org/data/2.5/weather"
# forceast used in program
another_api_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

# using 5 days --> every 3hour forecast data, NOTE: number of hours must match with cnt parameter
najskoriji = 0
in_3_hours = 1
in_6_hours = 2
in_9_hours = 3
in_12_hours = 4

time_stamps = (najskoriji, in_3_hours, in_6_hours, in_9_hours, in_12_hours)

parametres = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "units": "metric",
    "appid": api_key,
    "cnt": in_12_hours+1
}

response = requests.get(url=another_api_endpoint, params=parametres)
response.raise_for_status()

# weather_condition = response.json()["list"][in_6_hours]["weather"][0]["main"]
# description = response.json()["list"][in_6_hours]["weather"][0]['description']
# date_and_time = response.json()["list"][in_6_hours]["dt_txt"]

weather_data = response.json()
will_rain = False

for time in time_stamps:
    weather_id = int(weather_data["list"][time]["weather"][0]["id"])
    if weather_id < 701:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject:Weather alert\n\nHena, bring an UMBRELLA today!\n xoxo"
        )

# consider importing os to use environment variables:
# os.environ.get("SOME_VARIABLE_PUT_QUOTATIONS")
# you need to set the enviornment variables 1st though, click on current file, edit configurations, click on little plus
# choose python... set variables

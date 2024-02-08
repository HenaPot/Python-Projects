import requests
import datetime as dt


todays_date = dt.date.today()  # only used for testing
next_week_date = dt.date.today() + dt.timedelta(days=7)
last_date = next_week_date + dt.timedelta(days=6*30)

# print(todays_date.strftime("%d/%m/%Y"), last_date.strftime("%d/%m/%Y"))


class FlightData:
    # This class is responsible for structuring the flight data ---> SECOND PART OF THE TASK.

    def __init__(self):
        self.FLYING_FROM = "sarajevo_ba"
        self.API_KEY = "apikey"
        self.header = {
            "apikey": self.API_KEY
        }
        self.quary = {
            "fly_from": self.FLYING_FROM,
            "date_from": next_week_date.strftime("%d/%m/%Y"),
            "date_to": last_date.strftime("%d/%m/%Y"),
            "max_fly_duration": 27,
            "flight_type": "round"
        }
        self.endpoint = "https://api.tequila.kiwi.com/v2/search"
        self.pairs = []

    def add_pairs(self):
        self.pairs.clear()
        response = requests.get(url=self.endpoint, headers=self.header, params=self.quary)
        response.raise_for_status()
        dictionary = response.json()
        for index, flight in enumerate(dictionary["data"]):
            self.pairs.append((flight["cityTo"], str(response.json()["data"][index]["price"])))

    def get_link(self, city, price):
        response = requests.get(url=self.endpoint, headers=self.header, params=self.quary)
        response.raise_for_status()
        dictionary = response.json()
        for a_dict in dictionary["data"]:
            if a_dict["cityTo"] == city and str(a_dict["price"]) == str(price):
                return a_dict["deep_link"]

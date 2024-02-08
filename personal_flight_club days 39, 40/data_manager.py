import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.get_endpoint = "https://api.sheety.co/a6c2b664c897e7fc4d8ea48a15788c0a/flightDeals/prices"
        response0 = requests.get(url=self.get_endpoint)

        self.dictionary = response0.json()
        self.list_entries = self.dictionary["prices"]

    def get_cites(self):
        return [entry["city"] for entry in self.list_entries]

    def get_lowest_prices(self):
        return [entry["lowestPrice"] for entry in self.list_entries]
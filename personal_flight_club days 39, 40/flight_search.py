import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API --> FIRST PART OF THE TASK.

    def __init__(self):
        self.API_KEY = "genericAPIkey"
        self.header = {
            "apikey": self.API_KEY
        }

    def get_iata_code(self, city_name):
        query = {"term": f"{city_name}", "location_types": "city"}
        response = requests.get(url="https://api.tequila.kiwi.com/locations/query",
                                headers=self.header, params=query)
        response.raise_for_status()
        code = response.json()["locations"][0]["code"]
        return code

    def get_city_id(self, city_name):
        """
        Useful for defining location of departure (Sarajevo in my case)
        :param city_name:
        :return: id
        """
        query = {"term": f"{city_name}", "location_types": "city"}
        response = requests.get(url="https://api.tequila.kiwi.com/locations/query",
                                headers=self.header, params=query)
        response.raise_for_status()
        ID = response.json()["locations"][0]["id"]
        return ID


# flight_search = FlightSearch()
# print(flight_search.get_city_id("Sarajevo"))
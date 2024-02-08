# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.

import requests
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData


data = DataManager()
search = FlightSearch()
other_data = FlightData()

# UNCOMMENT THE CODE BELLOW and run ONLY WHEN THERE ARE CHANGES TO THE GOOGLE SHEET

# for index, city in enumerate(data.get_cites()):
#     json_params = {
#         "price": {"iataCode": search.get_iata_code(city)}
#     }
#     response1 = requests.put(url=f"{data.get_endpoint}/{index+2}", json=json_params)
#     response1.raise_for_status()


other_data.add_pairs()
pairs = other_data.pairs

lowest_prices_values = data.get_lowest_prices()
city_keys = data.get_cites()

formatted_dict = dict(zip(city_keys, lowest_prices_values))

for item in pairs:
    if item[0] in formatted_dict and int(item[1]) < formatted_dict[item[0]]:
        print(item[0], str(item[1])+"€")
        the_link = other_data.get_link(item[0], item[1])
        print(the_link)


import requests
import datetime as df


pixela_endpoint = "https://pixe.la/v1/users"
my_token = "tokencic"
my_username = "username"

user_parametres = {
    "token": my_token,
    "username": my_username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# once you create a user the code below is bugged
# response = requests.post(url=pixela_endpoint, json=user_parametres)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{my_username}/graphs"
headers = {
    "X-USER-TOKEN": my_token
}
graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "h",
    "type": "float",
    "color": "ajisai"
}

# once you create a graph the code below does not work
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# todays_date = df.date.today()
# the_date = str(todays_date).replace("-", "")

date = df.datetime.now()

single_pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}"
pixel_parametres = {
    "date": date.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? ")
}

# GET BACK OT THIS ONE AND UNCOMMENT WHEN NECESSARY
response = requests.post(url=single_pixel_endpoint, json=pixel_parametres, headers=headers)
print(response.text)


# update_pixel_endpoint = f"{single_pixel_endpoint}/{pixel_parametres['date']}"

# response = requests.delete(url=f"{single_pixel_endpoint}/{pixel_parametres['date']}", headers=headers)
#print(response.text)

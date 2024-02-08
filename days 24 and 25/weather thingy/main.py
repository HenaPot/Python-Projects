# days = []
# temperatures = []
# conditions = []
#
# with open("weather_data.csv") as data_file:
#     for line in data_file.readlines():
#         separated_values = line.split(sep=",")
#         days.append(separated_values[0])
#         temperatures.append(separated_values[1])
#         conditions.append(separated_values[2])
#
#
# print(days)
# print(temperatures)
# print(conditions)


# import csv
#
#
# days = []
# temperatures = []
# conditions = []
# index_counter = 0
# loop_running_1st_time = True
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         if loop_running_1st_time:
#             loop_running_1st_time = False
#             continue
#         days.append(row[0])
#         temperatures.append(int(row[1]))
#         conditions.append(row[2])
#
#
import pandas

# must always read the file first
data = pandas.read_csv(filepath_or_buffer="weather_data.csv")

# csv file is expressed as nested dictionary
# keys --> 1st row of the csv file
# values --> dictionary with {key-->index: value-->1st column of the file}
data_dictionary = data.to_dict()

# accessing temperature column from the csv file all of its values are put in a list
temp_list = data["temp"].to_list()

# max value in a column of a csv file found using pandas
maximum_temperature = data.temp.max()
# print(data[data.temp == maximum_temperature])


monday = data[data.day == "Monday"]
monday_temp_int = int(monday.temp)
# print(monday_temp_int)


def celsius_to_fahrenheit(num):
    return (num * 1.8) + 32


# print(celsius_to_fahrenheit(monday_temp_int))

import pandas


# must always read the file first
# uvijek prvo pročitati fajl
squirrels_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# accessing column containing primary fur colours and turning it into a list
# nan, empty values are dropped from the list
# pristupanje koloni koja sadrži primarne boje krzna i pretvaranje u listu
# nan, prazne vrijednosti se izbacuju sa liste
Fur_Color_List = list(squirrels_data["Primary Fur Color"].dropna())

# reformatting previous list to lowercase using list comprehension
# preformatiranje prethodne liste u mala slova
fur_color_list = [x.lower() for x in Fur_Color_List]

# unique entries of different fur colors extracted and turned into a list
# izvučeni jedinstveni unosi različitih boja krzna i pretvoreni u listu
possible_fur_colors = list(dict.fromkeys(fur_color_list))

# iteration over unique colors and all entries of each color;  occurrences for each are counted and stored into a list
# ponavljanje jedinstvenih boja i svih unosa svake boje; pojavljivanja za svaku se broje i pohranjuju u listu
count_list = []
for color in possible_fur_colors:
    counter = 0
    for squirrel_color in fur_color_list:
        if color == squirrel_color:
            counter += 1
    count_list.append(counter)

# created dictionary compatible with pandas
# kreiran rječnik kompatibilan s pandaasom
my_dict = {
    "Fur Color": possible_fur_colors,
    "Count": count_list
}

# refined data structure that neatly presents tables in 2D --> DataFrame
# prefinjena struktura podataka koja uredno predstavlja tabele u 2D --> DataFrame
final_data = pandas.DataFrame(my_dict)

# refined data written into a new file
# rafinirani podaci upisani u novi fajl
with open("squirrel color and count.csv", "w") as new_file:
    new_file.write(str(final_data))


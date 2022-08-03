# with open("./002 weather-data.csv") as weathers_file:
#    weather = weathers_file.readlines()
#    print(weather)


# import csv

# with open("./002 weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#    temperature = []
#    for row in data:
#        if row[1] != "temp":
#            temperature.append(int(row[1]))
#    print(temperature)

import pandas

data = pandas.read_csv("./002 weather-data.csv")
print(data["temp"])

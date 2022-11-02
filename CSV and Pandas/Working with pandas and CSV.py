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

data = pandas.read_csv("002 weather-data.csv")
# print(type(data))
# print(type(data["temp"]))

# create separate dictionary for each of the columns:
# data_dic = data.to_dict()
# print(data_dic)

# turn this data series into a python list:
temp_list = data["temp"].to_list()
print(len(temp_list))

average = sum(temp_list) / len(temp_list)
print(average)

# calculating the average of temperature:
print(data["temp"].mean())

# print the maximum value in temp series with call the max method:
print(data["temp"].max())

# get data in columns:
print(data["condition"])
# or:
print(data.condition)


# get data in rows:
print(data[data.day == "Monday"])
# print the row that has the highest temperature:
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
monday_temp = monday.temp
monday_temp_f = monday_temp * 9/5 + 32
print(monday_temp_f)

# create a dataframe from scratch:
data_dic = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data1 = pandas.DataFrame(data_dic)
data1.to_csv("new_data.csv")
# print(data1)


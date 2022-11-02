import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])
print(red_squirrel)
print(grey_squirrel)
print(black_squirrel)

data_dic = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel, red_squirrel, black_squirrel]
}

df = pandas.DataFrame(data_dic)
df.to_csv("Squirrel_count.csv")
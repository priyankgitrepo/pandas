import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
# print(data["condition"])

print(data[data.day == "Monday"])
print(data["temp"].max())
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(int(monday.temp))

temp_con = int(monday.temp)
temp = temp_con * 4

print(temp)

data_dict = {
    "students": ["Amy","James","Angela"],
    "scores": [76,56,65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")



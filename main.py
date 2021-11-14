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

print(f"the temp is : {temp}")

data_dict = {
    "students": ["Amy","James","Angela"],
    "scores": [76,56,65]
}
data_1 = pandas.DataFrame(data_dict)
data_1.to_csv("new_data.csv")

monday_len = len(data[data.day == "Monday"])
print(monday_len)


#print(data[data.day == "Monday"])
print(data[data.day == "Monday"])
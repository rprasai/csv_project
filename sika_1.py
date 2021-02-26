import csv

open_file = open("sitka_weather_07-2018_simple.csv", "r")
csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)

highs = []


# Exmaple
# somedate = "2018-07-01"
# converted_date = datetime.strptime(somedate, "%Y-%m-%d")
# print(converted_date)

for row in csv_file:
    highs.append(int(row[5]))


import matplotlib.pyplot as plt

plt.plot(highs, c="red")

plt.title("Daily high temperatures, July 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)


plt.show()

import csv
from datetime import datetime

# Sitka
open_file = open("sitka_weather_2018_simple.csv", "r")
csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)


# Creating Header Dictionary
si_header = {}
for index, column_header in enumerate(header_row):
    si_header[column_header] = index
#    print("Index:", index, "Column Name:", column_header)
# print(si_header)


highs = []
dates = []
lows = []


for row in csv_file:
    highs.append(int(row[si_header["TMAX"]]))
    converted_date = datetime.strptime(row[si_header["DATE"]], "%Y-%m-%d")
    dates.append(converted_date)
    lows.append(int(row[si_header["TMIN"]]))
    i = 0
    while i == 0:
        si_heading = row[si_header["NAME"]]
        i += 1
print(si_heading)

print(highs[:10])


print("****DEATH  VALLEY****")
# Death Valley
dv_open_file = open("death_valley_2018_simple.csv", "r")
dv_csv_file = csv.reader(dv_open_file, delimiter=",")


dv_header_row = next(dv_csv_file)


dv_header = {}
for index, column_header in enumerate(dv_header_row):
    dv_header[column_header] = index
#    print("Index:", index, "Column Name:", column_header)

dv_highs = []
dv_dates = []
dv_lows = []

for row in dv_csv_file:
    try:
        high = int(row[dv_header["TMAX"]])
        low = int(row[dv_header["TMIN"]])
        converted_date = datetime.strptime(row[dv_header["DATE"]], "%Y-%m-%d")
    except ValueError:
        print(f"Missing data for {converted_date}")
    else:
        dv_highs.append(int(row[dv_header["TMAX"]]))
        dv_lows.append(int(row[dv_header["TMIN"]]))
        dv_dates.append(converted_date)
        i = 0
        while i == 0:
            dv_heading = row[dv_header["NAME"]]
            i += 1

print(dv_heading)
# print(dv_highs[:10])

print("******PLOT*******")
import matplotlib.pyplot as plt

# assigning a 2 x 1 matrix for two plots
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, sharey=True)
fig.suptitle("Temperature comparision between " + si_heading + " and " + dv_heading)
fig.autofmt_xdate()


print("****Sikta PLOT*****")
ax1.plot(dates, highs, c="red")
ax1.plot(dates, lows, c="blue")
# filling the color between the lines
ax1.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
ax1.set_title(si_heading, fontsize=14)


print("*****DEATH VALLEY PLOT*****")
ax2.plot(dv_dates, dv_highs, c="red")
ax2.plot(dv_dates, dv_lows, c="blue")
# filling the color between the lines
ax2.fill_between(dv_dates, dv_highs, dv_lows, facecolor="blue", alpha=0.1)
ax2.set_title(dv_heading, fontsize=14)


plt.show()

import os
import datetime
import csv

command = "upower -i /org/freedesktop/UPower/devices/battery_BAT0"
result = os.popen(command).read()

dic = {(line.split(":")[0].strip()): line.split(":")[1].strip() for line in result.split("\n") if ":" in line}

print(dic["state"])
print(dic["energy"])
print(dic["energy-rate"])

# Adds a line to the CSV file
absolute_path = "/home/elias/Code/scripts/power_mesurment/batterie.csv"


with open(absolute_path, 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), float(dic["energy"][:-3].replace(",", ".")), float(dic["energy-rate"][:-2].replace(",", "."))])

with open(absolute_path.replace("batterie", "data"), 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), dic["energy"], dic["energy-rate"]])

    
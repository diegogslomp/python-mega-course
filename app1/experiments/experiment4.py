import csv
import os

filepath = os.path.join("files", "wheater.csv")

with open(filepath) as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")

for row in data[1:]:
    if row[0] == city:
        print(row[1])
        break

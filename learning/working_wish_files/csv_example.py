import csv
from learning import hell

File = "C:/users/ikriatov/file.csv"

users = [
    ["Ihor", 28],
    ["Slavik", 29],
    ["Ann", 23]
]


with open(File, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(users)

with open(File, "a", newline="") as file:
    users.append(["David", 15])
    writer = csv.writer(file)
    writer.writerow(users[-1])

with open(File, "r") as file:
    for item in file:
        hell.comma_separator(item, ',')

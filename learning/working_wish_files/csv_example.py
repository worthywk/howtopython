import csv
from learning import hell

File = "C:/users/ikriatov/file.csv"
File1 = "C:/users/ikriatov/file1.csv"

users = [
    ["Ihor", 28],
    ["Slavik", 29],
    ["Ann", 23]
]

users1 = [
    {'name': 'Ihor', 'age': 28},
    {'name': 'Slavik', 'age': 29},
    {'name': 'Ann', 'age': 23}
]

users1 = tuple(users1)

# Operations for File
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

with open(File, "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0], "-",row[1])

# Operations for File1

with open(File1, "w", newline="") as file1:
    writer = csv.DictWriter(file1, fieldnames=('name', 'age'))
    writer.writeheader()
    writer.writerows(users1)

    some_user = {'name': 'David','age': 15}
    writer.writerow(some_user)

with open(File1, "r", newline="") as file1:
    reader = csv.DictReader(file1)
    for user in reader:
        print(user['name'], "-", user['age'])

print(users)
print(users1)
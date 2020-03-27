import pickle

File = "files/users.dat"

users = [
    ["Ihor", 28],
    ["Slavik", 29],
    ["Ann", 23]
]

with open(File, "wb") as f:
    pickle.dump(users, f)

with open(File, "rb") as f:
    users_from_file = pickle.load(f)
    for user in users_from_file:
        print(f'Name: {user[0]}, Age: {user[1]}')

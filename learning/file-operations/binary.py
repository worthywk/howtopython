import pickle
import shelve


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

# working with shelve module

File1 = "files/friends_file"

friends = {
    "friend1": "Ihor",
    "friend2": "Slavik",
    "friend3": "Ann"
}

with shelve.open(File1) as f:
    f = friends
    for friend in f:
        print(f[friend])
    some_friend = f.get("friend4", "\nDavid is not словарь\n")
    print(some_friend)
    friends["friend4"] = "David"
    for friend in f:
        print(f[friend])
    f.pop("friend3", "\nAня is not dictionary")
    print(f.items())
    f["friend3"] = f.pop('friend4')
    print(f.items())
    del f['friend1']
    print(f.items())
    f.clear()
    print(f)
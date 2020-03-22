users = {"user_name1": "Ihor", "user_name2": "Slavik", "user_name3": "Ann"}

users_list = [
    ["Ihor", 28],
    ["Slavik", 29],
    ["Ann", 23]
]

users_tuple = (
    ("Ihor", 28),
    ("Slavik", 29),
    ("Ann", 23)
)

users_dict_from_list = dict(users_list)
users_dict_from_tuple = dict(users_tuple)

print(users_dict_from_list)  # {'Ihor': 28, 'Slavik': 29, 'Ann': 23}
print(users_dict_from_list["Ihor"])  # 28

users_dict_from_list["Ihor"] = users_dict_from_tuple["Slavik"]
print(users_dict_from_list["Ihor"])  # 29

users_dict_from_list["David"] = 15  # add new key - value
# users_dict_from_tuple["David"] # KeyError: 'David'

if "David" in users_dict_from_tuple:
    print(users_dict_from_list["нашли David"])
else:
    print("David is not словарь")

print(users_dict_from_list.get("David", "David is not словарь"))  # 15
print(users_dict_from_tuple.get("David", "David is not словарь"))  # David is not словарь, в отличии от 25 строки

if "David" in users_dict_from_list:
    del users_dict_from_list["David"]  # new operator "del" like if else and others
    print("David is not словарь now")
else:
    print("David is not словарь")

print(users_dict_from_list.pop("David", "David is not словарь опять"))  # David is not словарь опять
users_dict_from_tuple.pop("Ihor")  # will be deleted

print(users_dict_from_list, users_dict_from_tuple)

users_dict_from_tuple = users_dict_from_list  # reference!!!
users_dict_copy = users_dict_from_tuple.copy()
print(users_dict_from_list,
      users_dict_from_tuple)  # {'Ihor': 29, 'Slavik': 29, 'Ann': 23} {'Ihor': 29, 'Slavik': 29, 'Ann': 23}

users_dict_from_list["David"] = 15
print(users_dict_from_list,
      users_dict_from_tuple)  # {'Ihor': 29, 'Slavik': 29, 'Ann': 23, 'David': 15} {'Ihor': 29, 'Slavik': 29, 'Ann': 23, 'David': 15}
users_dict_from_list.clear()
print(users_dict_from_tuple)  # empty!!!
print(users_dict_copy)  # {'Ihor': 29, 'Slavik': 29, 'Ann': 23}

users_dict_copy.update({"David": 15})  # add new key - value
print(users_dict_copy)

for user in users_dict_copy:
    print(user, " - ", users_dict_copy[user])

    #    Ihor - 29
    #   Slavik - 29
    #   Ann - 23
    #   David - 15

for user_name, user_value in users_dict_copy.items():
    print(user_name, " - ", user_value)

    #    Ihor - 29
    #   Slavik - 29
    #   Ann - 23
    #   David - 15

for user_name in users_dict_copy.keys():
    print(user_name)

    #   Ihor
    #   Slavik
    #   Ann
    #   David

for user_value in users_dict_copy.values():
    print(user_value)

    # 29
    # 29
    # 23
    # 15

users_dict_copy.clear()

super_dict = {
    "Ihor": {"age": 28, "nickname": "worthy"},
    "Slavik": {"age": 29, "nickname": "scerny"},
    "Ann": {"age": 23, "nickname": "happyann"},
    "David": {"age": 15, "nickname": "ridov"}
}

print("simple mode")

for items in super_dict:
    print(items, super_dict[items])

print("normal mode")

for keys, values in super_dict.items():
    print(f'\n{keys}:')
    for key, value in values.items():
        print(key, value)

print("hard mode")

for keys in super_dict:
    print(f'\n{keys}:')
    for key in super_dict[keys]:
        print(key, " - ", super_dict[keys][key])

#  ЗАДАНИЕ: найти в словаре super_dict значение "ridov"

from learning import hell

users = {"Ihor", "Slavik", "Ann", "David", "Ihor"}

users1 = set(users)  # set with set
users2 = set(("Ihor", "Slavik", "Ann"))  # set with tuple
users3 = set(["Ihor", "Slavik", "Ann"])  # set with list

hell.delete_item_in_list("Thor", users1)  # Thor is not in list
users.discard("Ihor")
print(users1)
# {'Ihor', 'Ann', 'Slavik', 'David'}


users2.add("David")

print("users2: {users2}, users3: {users3}".format(users2=users2, users3=users3))
# users2: {'Ihor', 'Slavik', 'Ann'}, users3: {'Ihor', 'Slavik', 'Ann'}



print(users2.intersection((users3)))
print(users2 & users3)
# {'Ihor', 'Slavik', 'Ann'}

print(users2.difference(users3))
print(users2 - users3)
# {'David'}
from learning import hell

users = {"Ihor", "Slavik", "Ann", "David", "Ihor"}

users1 = set(users)  # set with set
users2 = set(("Ihor", "Slavik", "Ann"))  # set with list
users3 = set(["Ihor", "Slavik", "Ann"])  # set with tuple

users2.add("David")
print(users2)

hell.delete_item_in_list("Thor", users1)
users.discard("Ihor")
print(sorted(users1))  # ['Ann', 'David', 'Ihor', 'Slavik']

new_user = users3.union(users2)
users3.update(users2)
print(users3)
print(new_user)

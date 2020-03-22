# list
import copy

numbers1 = [1, 2, 3, 4, 5, 6]
print(numbers1)

numbers2 = [1] * 5
print(numbers2)

numbers3 = list(range(101))
print(numbers3)

numbers4 = list(range(1, 5))
print(numbers4)

numbers5 = list(range(1, 10, 2))
print(numbers5)

numbers6 = list(range(9, 0, -2))
print(numbers6)

companies1 = ["Microsoft", "Google", "microsoft", "Apple"]

companies2 = companies1  # reference!
companies3 = companies1[:]  # new list
companies4 = companies1.copy()  # new list
companies5 = copy.deepcopy(companies1)  # new list

companies6 = companies1[:2] + companies4[2:3]
print(companies6)

users = [
    ["Ihor", 28],
    ["Slavik", 29]
]

for user in users:
    for i in user:
        if i == users[-1][-1]:
            print(i)
        else:
            print(str(i) +", ",end="")
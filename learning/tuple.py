# tuple

user = ("Ihor", 28)
print(user)

user1 = "Slavik", 29
print(user1)

users2 = ("Ann",) # don't forget to "," if tuple

user_list = ["Slavik", "Ihor", "Ann" ]
name1, name2, name3 = user_list
print(name1, name2, name3)

user_tuple = tuple(user_list)

print(user_list[:])
print(user_tuple[:])

user_list[0] = "New"
#  user_tuple[0] = "New" - error!


countries = (
    ("Germany", 80.2, (("Berlin", 3.326), ("Hamburg", 1.718))),
    ("France", 66, (("Paris", 2.2), ("Marcel", 1.6)))
)

for country in countries:
    country_name, country_population, cities = country
    print("\nCounty name = {}, country population = {}\n".format(country_name, country_population))
    for city in cities:
        city_name, city_population = city
        print("City name = {}, City population = {}".format(city_name, city_population))

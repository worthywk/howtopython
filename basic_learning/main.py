from classes.person import *

people = [Person("Ihor", 28), Employee("Slavik", 29, "NovaPoshta"), Student("David", 15, "World of Warcraft")]

for human in people:
	if isinstance(human, Person):
		print("True"
			  )
	human.display_info()
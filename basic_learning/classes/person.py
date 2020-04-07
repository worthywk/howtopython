class Person:
    person = "Person"

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return self.__name, self.__age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Age is not valid")

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print("name: {}, age: {}".format(*self.__str__()))


class Employee(Person):

    def __init__(self, name, age, company):
        Person.__init__(self, name, age)
        self.__company = company

    def display_info(self):
        Person.display_info(self)
        print(self.__company)


class Student(Person):

    def __init__(self, name, age, university):
        Person.__init__(self, name, age)
        self.__university = university

    def display_info(self):
        print("Welcome to", self.__university)

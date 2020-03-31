class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1,100):
            self.__age = age
        else:
            print("Age is not valid")


    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(self.__name, self.__age)


class Employee(Person):

    def details(self, company):
        print(self.name, "is working in company", company)
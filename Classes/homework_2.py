class Pet:
    def __init__(self, name, species, age: int, gender):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__gender = gender

        def get_info():
            print(f'Name: {self.__name}, species: {self.__species}, age: {self.__age}, gender: {self.__gender}')


class Dog(Pet):
    def __init__(self, name, species, age: int, gender, breed):
        super().__init__(name, species, age, gender)
        self.__breed = breed

    def say(self):
        print("Гав!")


class Cat(Pet):
    def __init__(self, name, species, age: int, gender, color):
        super().__init__(name, species, age, gender)
        self.__color = color

    def say(self):
        print("Мяу!")
class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname = ""):
        self.name = newname
    def __str__(self):
        return "Animal:" + str(self.name) + ":" + str(self.age)

class Cat(Animal):
    ''''
    __init__ is not included here, it's inherited from Animal
    '''
    def speak(self):
        print("meow")
    def __str__(self):
        return "Cat:" + str(self.name) + ":" + str(self.age)

class Rabbit(Animal):
    def speak(self):
        print("meep")
    def __str__(self):
        return "Rabbit:" + str(self.name) + ":" + str(self.age)

class person(Animal):
    def __init__(self, name, age):
        return




castor = Cat(1)
castor.set_name("Castor")

pollux = Cat(2)
pollux.set_name("Pollux")

print(castor, pollux)
print(Animal.__str__(castor))
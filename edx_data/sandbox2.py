import random

class Animal(object):
    # superclass
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
    # subclass
    ''''
    __init__ is not included here, it's inherited from Animal
    '''
    def speak(self):
        print("meow")
    def __str__(self):
        return "Cat:" + str(self.name) + ":" + str(self.age)

class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1 = None, parent2 = None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag # this gets the value from the class variable 'tag'
        Rabbit.tag += 1 # updates the Rabbit.tag variable so that each new rabbit id is unique
    def speak(self):
        print("meep")
    def get_rid(self):
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __add__(self, other):
        return Rabbit(0, self, other)
    def __eq__(self, other):
        parents_same = self.parent1.rid == other.parent2.rid and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite

    def __str__(self):
        return "Rabbit:" + str(self.name) + ":" + str(self.age)

class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)  # call Animal constructor
        Animal.set_name(self, name) # call Animal method
        self.friends = []

    def get_friends(self):
        return self.friends

    def add_friends(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        print("Hello")

    def age_diff(self, other):
        # alternative : diff = self.age - other.age
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name, "is", diff, "years older than", other.name)
        else:
            print(self.name, "is", diff, "years younger than", other.name)

    def __str__(self):
        return "person:" + str(self.name) + ":" + str(self.age)

class Student(Person):
    # inherits from Person and therefore also from Animals
    def __init__(self, name, age, major = None):
        Person.__init__(self, name, age)
        self.major = major

    def change_major(self, major):
        self.major = major

    def speak(self):
        r = random.random()
        if r < 0.25:
            print("homework")
        elif 0.25 <= r < 0.5:
            print("sleep")
        elif 0.5 <= r < 0.75:
            print("eat")
        else:
            print("watch tv")

    def __str__(self):
        return "student:" + str(self.name) + ":" + str(self.age) + ":" + str(self.major)



'''
castor = Cat(1)
castor.set_name("Castor")

pollux = Cat(2)
pollux.set_name("Pollux")

third = Rabbit(3)
third.set_name()

print(castor, pollux, third)
print(Animal.__str__(castor))

eelco = Person("Eelco", 37)
peta = Person ("Peta", 30)

print(eelco, peta)

eelco.age_diff(peta)
Person.age_diff(peta, eelco)
Person.age_diff(eelco, peta)

kagney = Student("Kagney", 34)
audrey = Student("Audrey", 35)

print(kagney, audrey)
kagney.speak()

'''

peter = Rabbit(2)
peter.set_name("Peter")
hopsy = Rabbit(3)
hopsy.set_name("Hopsy")

popsy = peter + hopsy
popsy.set_name("Popsy")

cotton = Rabbit(1, peter, hopsy)
cotton.set_name("Cotton")


print(popsy == cotton)
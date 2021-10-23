import datetime

class Person(object):
    def __init__(self, name):
        # create a blank person
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1] # splits the string into strings and returns the last string
    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.lastName
        return self.lastName < other.lastName
    def __str__(self):
        return self.name

    def getLastName(self):
        # return last name
        return self.lastName
    def setBirthday(self, m, d, y):
        self.birthday = datetime.date(y, m, d)
    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

class MITPerson(Person):
    nextId = 1
    def __init__(self, name):
        Person.__init__(self, name)
        self.id = MITPerson.nextId
        MITPerson.nextId += 1

    def getIdNum(self):
        return self.id

    def __lt__(self, other):
        return self.id < other.id

    def speak(self, utterance):
        return (self.getLastName() + "says: " + utterance)



p1 = Person("Peta Jensen")
p1.setBirthday(12, 24, 1990) # 24 december
p2 = Person("Audrey Bitoni")
p2.setBirthday(8, 16, 1986) # 16 augustus
p3 = Person("Eve Lawrence")
p3.setBirthday(10, 4, 1985) # 4 oktober

personList = [p1, p2, p3]


personList.sort()

for e in personList:
    print(e)
class Cat:
    species = "mammal"
    legs = 4
    eyes = 2
    tail = 1

    def __init__(self, name, age)
        self.name = name
        self.age = age

    def description(self):
        return "{} is {} years old".format(self.name, self.age)

gus = Cat("Gus", 9)
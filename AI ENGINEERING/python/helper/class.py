class Dog:
    def __init__(self, name, age):  # runs on creation
        self.name = name            # instance data
        self.age = age

    def bark(self):                 # instance method
        print(f"{self.name} says: Woof!")

    def birthday(self):
        self.age += 1               # mutates this instance's data
        print(f"{self.name} is now {self.age}")

d = Dog("Rex", 3)
d.bark()        # Rex says: Woof!
d.birthday()    # Rex is now 4
d.birthday()    # Rex is now 5

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printDetails(self, name, age):
        print(f"the name is {name} and age is {age}")

dhanush = person("dhanushkumar", 21)
sanjay = person("sanjaykumar", 20)

print(dhanush.name)
print(dhanush.age)

print(sanjay.name)
print(sanjay.age)


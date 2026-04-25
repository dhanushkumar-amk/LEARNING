
class Person:
    def __init__(self, name, age, isAlive):
        self.name = name
        self.age = age
        self.isAlive = isAlive

    def printDetails(self):
        print(f"the name is {self.name} and age is {self.age} and isAlive is {self.isAlive}")

class Student(Person):
    def __init__(self, name, age, isAlive, rollNo, grade):
        super().__init__(name, age, isAlive)
        self.rollNo = rollNo
        self.grade = grade

    def printDetails(self):
        print(f"the name is {self.name} and age is {self.age} and isAlive is {self.isAlive} and rollNo is {self.rollNo} and grade is {self.grade}")

class Teacher(Person):
    def __init__(self, name, age, isAlive, subject, salary):
       super().__init__(name, age, isAlive)
       self.subject = subject
       self.salary = salary

    def printDetails(self):
        print(f"the name is {self.name} and age is {self.age} and isAlive is {self.isAlive} and subject is {self.subject} and salary is {self.salary}")


dhanush = Student("Dhanush", 20, True, 1, "A")
sanjay = Student("sanjay", 20, True, 2, "B")

nirja = Teacher("Raj", 26, False, "Maths", 100000)

print(dhanush.printDetails())
print(sanjay.printDetails())
print(nirja.printDetails())

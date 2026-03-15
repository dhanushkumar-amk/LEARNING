# Simple Inheritance Example in Python

# Parent class (Base class)
class Vehicle:
    def __init__(self, noOfWheels=0, milage=0.0):   # default values added
        self.noOfWheels = noOfWheels
        self.milage = milage

    def move(self):
        print("Vehicle is moved")

    def stop(self):
        print("Vehicle is stopped")


# Child class (inherits from Vehicle)
class Car(Vehicle):
    def __init__(self, noOfWheels=0, milage=0.0, noOfAirbags=0):  # default values added
        super().__init__(noOfWheels, milage)   # calls Vehicle's __init__
        self.noOfAirbags = noOfAirbags

    # Overriding parent methods (Method Overriding)
    def move(self):
        print("Car is moved")

    def stop(self):
        print("Car is stopped")

    def __del__(self):
        print("Car is deleted")

    def __str__(self):
        return f"Car(wheels={self.noOfWheels}, milage={self.milage}, airbags={self.noOfAirbags})"

    # Getters
    def getNoOfWheels(self):
        return self.noOfWheels

    def getMilage(self):
        return self.milage

    def getNoOfAirbags(self):
        return self.noOfAirbags

    # Setters
    def setNoOfWheels(self, noOfWheels):
        self.noOfWheels = noOfWheels

    def setMilage(self, milage):
        self.milage = milage

    def setNoOfAirbags(self, noOfAirbags):
        self.noOfAirbags = noOfAirbags


# car1 - using default values (no arguments)
print("--- car1 (default values) ---")
car1 = Car()
print(car1.getNoOfWheels())   # 0
print(car1.getMilage())       # 0.0
print(car1.getNoOfAirbags())  # 0
car1.move()
car1.stop()

print()

# car2 - using custom values
print("--- car2 (custom values) ---")
car2 = Car(4, 20.0, 6)
print(car2.getNoOfWheels())   # 4
print(car2.getMilage())       # 20.0
print(car2.getNoOfAirbags())  # 6
car2.move()
car2.stop()


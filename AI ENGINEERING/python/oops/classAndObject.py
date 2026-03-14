class Car:

    def __init__(self, noOfWheels=0, milage=0.0, noOfAirbags=0):
        print("Car is created")
        self.__noOfWheels = noOfWheels
        self.__milage = milage
        self.__noOfAirbags = noOfAirbags

    def move(self):
        print("Car is moved")

    def stop(self):
        print("Car is stopped")

    def __del__(self):
        print("Car is deleted")

    def __str__(self):
        return f"Car(wheels={self.__noOfWheels}, milage={self.__milage}, airbags={self.__noOfAirbags})"

    def getNoOfWheels(self):
        return self.__noOfWheels

    def setNoOfWheels(self, noOfWheels):
        self.__noOfWheels = noOfWheels

    def getMilage(self):
        return self.__milage

    def setMilage(self, milage):
        self.__milage = milage

    def getNoOfAirbags(self):
        return self.__noOfAirbags

    def setNoOfAirbags(self, noOfAirbags):
        self.__noOfAirbags = noOfAirbags


car1 = Car()
print(car1.getNoOfWheels())
print(car1.getMilage())
print(car1.getNoOfAirbags())
car1.move()
car1.stop()

print("---")

car2 = Car(4, 20.0, 6)
print(car2.getNoOfWheels())
print(car2.getMilage())
print(car2.getNoOfAirbags())
car2.move()
car2.stop()

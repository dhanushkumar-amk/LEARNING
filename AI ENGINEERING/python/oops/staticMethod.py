class Car:
    @staticmethod
    def moveForward():
        print("hello world")

    def moveBackward(self):
        print("Move backward")


Car1 = Car()
Car1.moveBackward()

Car.moveForward()

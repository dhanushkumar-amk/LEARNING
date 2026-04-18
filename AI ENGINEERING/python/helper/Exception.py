
num  = int(input("Enter the number : "))

try:
    division = num / 0
    print(division)
except ValueError:
    print("The given number is not a valid value")
except ZeroDivisionError:
    print("Can't divide by zero!")
finally:
    print("program execetuted successfully")



# custom Exception
class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(f"Cannot withdraw {amount}, balance is only {balance}")

# using it
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(amount, balance)
    return balance - amount

try:
    withdraw(100, 250)
except InsufficientFundsError as e:
    print(e)   # Cannot withdraw 250, balance is only 100


num  = int(input("Enter the number : "))
try:
    print(num)
except (ValueError, ZeroDivisionError):
    print("Error : ")
else:
    print("In this porgram no error found")
finally:
    print("program execetuted successfully")

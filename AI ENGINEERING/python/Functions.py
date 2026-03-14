def hello():
    print("Hello World")

hello()

# function with parameters
def hello(name):
    print("Hello", name)

hello("dhanushkumar")

# function with return value
def add(a, b):
    return a + b

sum = add(10, 20)
print(sum)

# function with default parameters
def hello(name = "John"):
    print("Hello", name)

hello()
hello("dhanushkumar")

# function with arbitrary arguments
def hello(*args):
    print("Hello", args)

hello("dhanushkumar", "John", "Doe")

# function with keyword arguments
def hello(**kwargs):
    print("Hello", kwargs)

hello(name="dhanushkumar", age=20, city="New York")


# recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

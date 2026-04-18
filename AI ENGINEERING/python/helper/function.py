
#  basic function
def fun(a, b):
    return a + b

print(fun(40, 60))

# default paramater
def default(name, age=21):
    print(f" {name} and age of the  {age}")

default("Dhanushkumar")

def varugunets(*args):
    print(args)
    sum = 0
    for i in args:
        sum += i
    print(sum)

varugunets(1,2,3,4,5,6,7,8,9,10)

# varaible argument
def show_info(**kwargs):
    print(kwargs)         # {'name': 'Alice', 'age': 25, 'city': 'Chennai'}
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Alice", age=25, city="Chennai")


# lambda
sqaure = lambda a : a * a
add = lambda a, b : a + b
power = lambda a : a ** a

print(add(10, 20))
print(sqaure(5))
print(power(2))

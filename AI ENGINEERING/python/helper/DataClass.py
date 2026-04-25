
from dataclasses import dataclass

@dataclass
class Person:
    name : str
    age : int
    email : str

dhanush = Person("Dhanushkumar", 21, "dhanushkumaramk@gmail.com")
print(dhanush)

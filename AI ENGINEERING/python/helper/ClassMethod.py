class Dog:
    species = "Canis lupus"
    count = 0

    def __init__(self, name):
        self.name = name
        Dog.count += 1

    @classmethod
    def get_species(cls):
        return cls.species              # access class variable

    @classmethod
    def from_string(cls, data):         # alternative constructor
        name = data.strip().title()
        return cls(name)                # calls Dog(name)

    @classmethod
    def get_count(cls):
        return f"{cls.count} dogs created"


d1 = Dog.from_string("  rex  ")        # alternative constructor
d2 = Dog("Buddy")

print(d1.name)              # Rex
print(Dog.get_species())    # Canis lupus
print(Dog.get_count())      # 2 dogs created

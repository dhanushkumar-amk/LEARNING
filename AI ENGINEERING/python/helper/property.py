class Circle:
    def __init__(self, radius):
        self._radius = radius           # _radius = private by convention

    @property
    def radius(self):                   # getter
        return self._radius

    @radius.setter
    def radius(self, value):            # setter
        if value < 0:
            raise ValueError("Radius can't be negative")
        self._radius = value

    @radius.deleter
    def radius(self):                   # deleter
        del self._radius

    @property
    def area(self):                     # computed, read-only property
        return 3.14 * self._radius ** 2


c = Circle(5)
print(c.radius)     # 5      ← looks like attribute access
print(c.area)       # 78.5   ← computed on the fly

c.radius = 10       # calls the setter
print(c.area)       # 314.0

c.radius = -1       # raises ValueError

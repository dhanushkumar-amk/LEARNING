class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0

# Call on class directly — no instance needed
print(MathUtils.add(3, 4))      # 7
print(MathUtils.is_even(10))    # True

# Also callable on an instance (but unusual)
m = MathUtils()
print(m.add(1, 2))              # 3

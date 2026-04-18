name = "Alice"
age = 30

# Basic usage
print(f"Hello, {name}! You are {age} years old.")
# → Hello, Alice! You are 30 years old.

# Expressions inside {}
print(f"Next year you'll be {age + 1}")
# → Next year you'll be 31

# Calling methods inside {}
print(f"Uppercase: {name.upper()}")
# → Uppercase: ALICE

# Formatting numbers
pi = 3.14159
print(f"Pi to 2 decimal places: {pi:.2f}")
# → Pi to 2 decimal places: 3.14

# Padding & alignment
print(f"{'left':<10}|{'center':^10}|{'right':>10}")
# → left      |  center  |     right

# Debugging with = (Python 3.8+)
x = 42
print(f"{x = }")
# → x = 42

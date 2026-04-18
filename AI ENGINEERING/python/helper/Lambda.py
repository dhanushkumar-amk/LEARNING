
square = lambda a : a * a
print(square(7))



# multiple arguments
add      = lambda x, y: x + y
multiply = lambda x, y, z: x * y * z

print(add(3, 5))           # 8
print(multiply(2, 3, 4))   # 24


# Default param
greet = lambda name="stranger": f"Hello, {name}!"
print(greet())           # Hello, stranger!
print(greet("dhanushkumar"))    # Hello, Alice!

# Inline if/else (ternary)
even_odd = lambda n: "Even" if n % 2 == 0 else "Odd"
print(even_odd(4))   # Even
print(even_odd(7))   # Odd

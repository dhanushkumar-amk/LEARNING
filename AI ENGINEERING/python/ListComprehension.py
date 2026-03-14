
arr = [1, 2, 3, 4, 5, 6]

# without comprehension
odd = []
even = []

for i in arr:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(odd)
print(even)

# list comprehension
odd = [i for i in arr if i % 2 != 0]
even = [i for i in arr if i % 2 == 0]
print(odd)
print(even)

# list comprehension with if-else
# odd = [i if i % 2 != 0 else "even" for i in arr]
# print(odd)

# list comprehension with nested for loop
# odd = [i for i in arr for j in arr if i % 2 != 0]
# even = [i for i in arr for j in arr if i % 2 == 0]
# print(odd)
# print(even)

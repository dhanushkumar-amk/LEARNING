
list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# method 1
for i in range(len(list)):
    print(list[i])

# method 2
for i in list:
    print(i)

# method 3
i = 0
while i < len(list):
    print(list[i])
    i += 1

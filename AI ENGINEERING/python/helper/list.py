list = [1,2,3,4,5,5,5,5]

list.remove(5)
list.append(7)

print(list.count(5))
list.reverse()


print(list[0])
print(list[-1])

print(list)

print(list[::-1])

for i in list:
    print(i, sep=" - ", end="\t")

for i in range(len(list)):
    print(list[i])


data = [1, "hello", True]
print(data)

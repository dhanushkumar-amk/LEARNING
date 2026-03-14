
#  create a  list
list = [1, 2, 3, 4, 5]

# print list
print(list)

# reverse a list
print(list[::-1])


#  union of list
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list3 = list1 + list2
print(list3)


# list replication
print(list * 3)

# length of list
print(len(list))

# insert the element in a list
print(list1)
list1.append(89)
print(list1)

# add multiple element
list1.extend(list2)  # list1 = list1 + list2
print(list1)

# insert at a particular position
list1.insert(2, 56)
print(list1)

# clear the list
# list1.clear()
print(list1)

# reverse the list
list1.reverse()
print(list1)

# remove the element
list1.remove(56)
print(list1)

# pop the element (remove the last element)
list1.pop()
print(list1)

# index of element
print(list1.index(4))

# count of element
print(list1.count(4))

# sort the list
list1.sort()
print(list1)

# copy the list
list2 = list1.copy()
print(list2)

# reverse the list
list2.reverse()
print(list2)

# minimum element
print(min(list2))

# maximum element
print(max(list2))

# maximum element
print(max(list2))

# sum of elements
print(sum(list2))


# iteration of a list
for i in list2:
    print(i)

# revsere sorting
list2.sort(reverse=True)
print(list2)

# nested list
nestedList = [
    [1, 2],
    [3, 4],
    [5, 6]
]
print(nestedList)
print(nestedList[0][0])

# iterate the nested list
for i in nestedList:
    for j in i:
        print(j, end=" ", sep=" ")
    print()




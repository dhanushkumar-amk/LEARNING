set = {1, 2, 3, 4, 5, 6}
print(set)

# add elements to set
set.add(7)
print(set)

# remove elements from set
set.remove(7)
print(set)

# union of two sets
set2 = {6, 7, 8, 9, 10}
print(set.union(set2))

# intersection of two sets
print(set.intersection(set2))

# difference of two sets
print(set.difference(set2))

# symmetric difference of two sets
print(set.symmetric_difference(set2))

# check if element is in set
print(5 in set)

# check if element is not in set
print(11 not in set)

# length of set
print(len(set))

# clear set
set.clear()
print(set)



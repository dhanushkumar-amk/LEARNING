nums = {1, 2, 3, 3, 4, 4}
print(nums)          # {1, 2, 3, 4}  ← duplicates removed

nums.add(5)
nums.discard(2)
print(nums)          # {1, 3, 4, 5}

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)   # Union:        {1, 2, 3, 4, 5}
print(a & b)   # Intersection: {3}
print(a - b)   # Difference:   {1, 2}

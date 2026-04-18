# [expression  for item in iterable  if condition]
#  ──────────  ──────────────────────  ───────────
#   what to       loop                  filter
#   produce                             (optional)


# Old way — for loop
squares = []
for x in range(1, 6):
    squares.append(x ** 2)

# ✅ List comprehension
squares = [x * 2 for x in range(1, 6)]
print(squares)    # [2, 4, 6, 8, 10]


# examples

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# only filter
evens  = [x for x in nums if x % 2 == 0]
print(evens)       # [2, 4, 6, 8, 10]

# only filter
big    = [x for x in nums if x > 6]
print(big)         # [7, 8, 9, 10]

# Both transform AND filter
even_sq = [x**2 for x in nums if x % 2 == 0]
print(even_sq)     # [4, 16, 36, 64, 100]

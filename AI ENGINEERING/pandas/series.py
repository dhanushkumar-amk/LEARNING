import pandas as pd

# what is a series in pandas?
# a series is a one-dimensional labeled array capable of holding any data type

# always starts from zero index
arr = pd.Series([1,2,3,4,5])
print(arr)

print(type(arr))

# check values form series
print(arr.values)

# check index form series
print(arr.index)

# check data type form series
print(arr.dtype)

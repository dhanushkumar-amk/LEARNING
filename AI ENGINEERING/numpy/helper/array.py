
import numpy as np


OneDArray = np.array([1,2,3,4,5])
print(OneDArray)

twoDArray = np.array([[1,2,3,4],[5,6,7,8]])
print(twoDArray)

threeDArray = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(threeDArray)


# checking dimenison in array
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)  # 0 dimension
print(b.ndim) # 1 dimenison
print(c.ndim) #2 dimension
print(d.ndim) #3 dimension

# slicing
# [start:end:step].

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[2:5])
print(arr[1:5:2])
print(arr[:6:2])
print(arr[::2])


# shapes

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape) # returns (2,4) which means 2 rows and 4 columns



# iteration
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)

# joining array
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))
print(arr)

# sort
print(np.sort(arr))
# boolen array sort
bol = np.array([True, False, True])
print(np.sort(bol))

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

#  slice => start:stop:step
print(arr[1:10:2])

#  start to end
print(arr[1:])
print(arr[:10])

# reversed
print(arr[::-1])
print(arr[10: 0: -2])


# matrix slicing
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix[0:2, 0:2])

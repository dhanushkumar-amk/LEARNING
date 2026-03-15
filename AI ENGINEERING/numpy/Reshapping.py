import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])



#  difference between flatten and ravel
# flatten => creates a copy of the array
# ravel => creates a view of the array

#  difference between reshape and ravel
# reshape => creates a copy of the array
# ravel => creates a view of the array

#  difference between flatten and reshape
# flatten => creates a copy of the array
# reshape => creates a view of the array


#  convert 1d array to 2d array
print(arr.reshape(2,5))

#  convert 2d array to 1d array
print(arr.flatten())

#  convert 2d array to 3d array
# print(arr.reshape(2,5,1))

#  convert 3d array to 2d array
# print(arr.reshape(2,5))

print(arr.ravel())


# transpose

mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(mat.T)

print(mat.swapaxes(0,1)) # same as transpose

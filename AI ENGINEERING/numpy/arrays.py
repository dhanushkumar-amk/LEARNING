import numpy as np

# check version
print(np.__version__)

# create an 1D array
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr)

# create an 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(arr2)

# create an 3D array
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3)

# type of an array
print(type(arr))
print(type(arr2))
print(type(arr3))

# shape of an array
print(arr.shape) # shows the rows and colums count
print(arr2.shape)
print(arr3.shape)

# size of an array
print(arr.size)
print(arr2.size)
print(arr3.size)

# ndim of an array says what type of dimmenison
print(arr.ndim)
print(arr2.ndim)
print(arr3.ndim)

# datatype of an array
print(arr.dtype)
print(arr2.dtype)
print(arr3.dtype)

# int -> float -> string -> boolean
arr4 = np.array([1, 2, 3, 4, 5, 6])
print(arr4.dtype)
arr4 = arr4.astype(float)
print(arr4.dtype)
arr4 = arr4.astype(str)
print(arr4.dtype)
arr4 = arr4.astype(bool)
print(arr4.dtype)


# create an array of zeros
print(np.zeros((2, 3)))

# create an array of ones
print(np.ones((2, )))

# create an array of random numbers
print(np.random.rand(2, 3))

# create an array of random integers
print(np.random.randint(0, 10, (2, 3)))

# create an array of random floats
print(np.random.uniform(0, 10, (2, 3)))

# create a array  constant value
print(np.full((2, 3), "hello"))

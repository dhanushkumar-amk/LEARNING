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


# zeros
print(np.zeros(4))
print(np.zeros((2,3)))

# ones
print(np.ones((2,5)))

# arrange
print(np.arange(0, 10, 2)) # returns 0 to 9 with step of 2

# linespace
print(np.linspace(0,10,5)) # returns 5 numbers between 0 and 10


arr = np.array([1,2,3,4,5])
arr2 = np.array([[1,2,3,4,5], [7,8,9,10,6]])
arr3 = np.array([[1,2,3],[4,5,6],[7,8,9]])

# shape
print(np.shape(arr)) # returns 5 which is 1 dimension
print(np.shape(arr2)) # it is two dimension array 2 rows and 5 colums each
print(np.shape(arr3)) # it is two dimension array 3 rows and 3 colums each


# Number of dimensions
print(np.ndim(arr)) # 1
print(np.ndim(arr2)) # 2
print(np.ndim(arr3)) # 2

# Indexing and Slicing
arr = np.arange(10)   # [0, 1, 2, ..., 9]

print("arr[3]:", arr[3])
print("arr[2:7]:", arr[2:7])
print("arr[::2]:", arr[::2])      # every second element
print("arr[::-1]:", arr[::-1])    # reverse
print(arr[::5]) # returns 0 5

# flattan convert multi dimenisonal array to 1d array
matrix = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(matrix.flatten())

# reshape is used to change the shape of array
arr = np.array([1,2,3,4,5,6,7,8,9,0])
print(arr.reshape(2,5)) # 2 row and 5 column
print(arr.reshape(5,2)) # 5 row and 2 column
print(arr.reshape(1,10)) # 1 row and 10 column
print(arr.reshape(10,1)) # 10 row and 1 column

# Transpose
matrix = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(matrix.T)
print(matrix.T.shape)

# Arthemetic Operation
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)

# Dot product
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Dot product (1D):", np.dot(a, b))        # 1*4 + 2*5 + 3*6 = 32

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Matrix multiplication:\n", A @ B)  #


#  Broadcasting
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

scalar = 10
print("Add scalar (broadcasting):\n", arr + scalar)

vector = np.array([100, 200, 300])
print("Add row vector:\n", arr + vector)

# Aggregate function
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("Sum:", np.sum(arr))           # 21
print("Sum along rows (axis=1):", np.sum(arr, axis=1))  # sum along rows
print("Mean:", np.mean(arr)) # mean or average of the array elements
print("Standard deviation:", np.std(arr)) # deviation from the mean
print("Max:", np.max(arr)) # maximum value
print("Min:", np.min(arr)) # minimum value

# Boolean indexing
arr = np.array([1, 3, 5, 7, 9, 2, 8])

mask = arr > 5
print("Boolean mask:", mask) # return true or false based on the condition => [False False False  True  True False  True]
print("Elements > 5:", arr[mask]) # return the elements that satisfy the condition => [7 9 8]
# or directly:
print("Elements > 5:", arr[arr > 5]) # return the elements that satisfy the condition => [7 9 8]


# np.where()
# np.where(condition, x, y) returns elements from x where condition is True, otherwise from y. Very useful for conditional replacement.

arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(np.where(arr % 2 == 0, "Even", "Odd")) # returns Even where condition is true otherwise Odd => ['Odd' 'Even' 'Odd' 'Even' 'Odd' 'Even' 'Odd' 'Even' 'Odd' 'Even']


# covaraiance and corelation
arr = np.array([1,2,3,4,5])
arr2 = np.array([10,20,30,40,50])

# covariance
#  covarinace tells us the direction of the linear relationship between the two arrays.
#  corelation tells us the strength of the linear relationship between the two arrays.

# positive covariance tells us that the two arrays are positively correlated
# negative covariance tells us that the two arrays are negatively correlated
# zero covariance tells us that the two arrays are not correlated

# positive corelation tells us that the two arrays are positively correlated
# negative corelation tells us that the two arrays are negatively correlated
# zero corelation tells us that the two arrays are not correlated

print(np.cov(arr, arr2)) # [[2.5  25. ]
                        #  [25.  250. ]]  -> it is covariance matrix

# corelation
print(np.corrcoef(arr, arr2)) # [[1.  1.]
                            # [1.  1.]] -> it is corelation matrix

# mean median mode
arr = np.array([1,2,3,4,5, 5, 5])

# mean => add all and divide by number of elements
print(np.mean(arr)) # (1+2+3+4+5+5+5) / 7 = 25 / 7 = 3.5714285714285716

# median => middle value when sorted
print(np.median(arr)) # [1, 2, 3, 4, 5, 5, 5] -> middle value is 4

# mode => most frequent values
print(np.mode(arr)) # 5


# Probabilty distribution
#  Probabilty distribution means showing the probability of each value in a dataset.

# types of distribution
# 1. normal distribution
# 2. binominal distribution
# 3. poisson distribution
# 4. uniform distribution
# 5. exponential distribution
# 6. t distribution
# 7. chi-square distribution
# 8. f distribution


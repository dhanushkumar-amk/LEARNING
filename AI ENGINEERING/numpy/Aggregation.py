import numpy as np

a = np.array([1, 2, 13, 4, 5])

# sum of all elements
print("sum : ",np.sum(a))

# minimum element
print("minimum : ",np.min(a))

# maximum element
print("maximum : ",np.max(a))

# mean of all elements
print("mean : ",np.mean(a))

# median of all elements
print("median : ",np.median(a))

# standard deviation means how much the data is spread out from the mean
print("standard deviation : ",np.std(a))

# variance means square of standard deviation variance formula = sum of (x - mean)^2 / n example => (1-5)^2 + (2-5)^2 + (13-5)^2 + (4-5)^2 + (5-5)^2 / 5
print("variance : ",np.var(a))

# index of min and max means position of min and max
print("index of min : ",np.argmin(a))
print("index of max : ",np.argmax(a))


# matrix

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)

# sum of all elements
print("sum : ",np.sum(matrix))

# minimum element
print("minimum : ",np.min(matrix))

# maximum element
print("maximum : ",np.max(matrix))

# mean of all elements
print("mean : ",np.mean(matrix))

# median of all elements
print("median : ",np.median(matrix))

# standard deviation means how much the data is spread out from the mean
print("standard deviation : ",np.std(matrix))

# variance means square of standard deviation variance formula = sum of (x - mean)^2 / n example => (1-5)^2 + (2-5)^2 + (13-5)^2 + (4-5)^2 + (5-5)^2 / 5
print("variance : ",np.var(matrix))

# index of min and max means position of min and max
print("index of min : ",np.argmin(matrix))
print("index of max : ",np.argmax(matrix))

# axis in  matrix axix means rows and columns 0 means columns and 1 means rows
print("sum of axis 0 : ",np.sum(matrix, axis=0))
print("sum of axis 1 : ",np.sum(matrix, axis=1))
print("minimum of axis 0 : ",np.min(matrix, axis=0))
print("minimum of axis 1 : ",np.min(matrix, axis=1))
print("maximum of axis 0 : ",np.max(matrix, axis=0))
print("maximum of axis 1 : ",np.max(matrix, axis=1))
print("mean of axis 0 : ",np.mean(matrix, axis=0))
print("mean of axis 1 : ",np.mean(matrix, axis=1))
print("median of axis 0 : ",np.median(matrix, axis=0))
print("median of axis 1 : ",np.median(matrix, axis=1))
print("standard deviation of axis 0 : ",np.std(matrix, axis=0))
print("standard deviation of axis 1 : ",np.std(matrix, axis=1))
print("variance of axis 0 : ",np.var(matrix, axis=0))
print("variance of axis 1 : ",np.var(matrix, axis=1))
print("index of min of axis 0 : ",np.argmin(matrix, axis=0))
print("index of min of axis 1 : ",np.argmin(matrix, axis=1))
print("index of max of axis 0 : ",np.argmax(matrix, axis=0))
print("index of max of axis 1 : ",np.argmax(matrix, axis=1))

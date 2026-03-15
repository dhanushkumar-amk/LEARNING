import numpy as np

a = np.array([[1, 2, 4, 5], [6, 7, 8, 9], [10, 11, 12, 13], [14, 15, 16, 17]])
b = np.array([[1, 2, 4, 5], [6, 7, 8, 9], [10, 11, 12, 13], [14, 15, 16, 17]])


# matrix multiplication
# first way
print("matrix multiplication : ",a @ b)

# second way
x = np.matmul(a, b)
print("matrix multiplication : ",x)

# third way
y = np.dot(a, b)
print("matrix multiplication : ",y)


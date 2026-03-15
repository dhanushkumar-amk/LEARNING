import numpy as np
from numpy.linalg import inv
from scipy.linalg import lu, expm, logm, sqrtm

# Using an invertible (non-singular) matrix
a = np.array([[2, 1, 3, 4],
              [5, 7, 2, 1],
              [3, 2, 8, 6],
              [1, 4, 5, 9]], dtype=float)

b = np.array([[1, 0, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 1, 2],
              [3, 4, 5, 6]], dtype=float)


# matrix multiplication
# first way
print("matrix multiplication :\n", a @ b)

# second way
x = np.matmul(a, b)
print("matrix multiplication :\n", x)

# third way
y = np.dot(a, b)
print("matrix multiplication :\n", y)

# inverse of matrix
print("inverse of matrix :\n", inv(a))

# determinant of matrix
print("determinant of matrix :", np.linalg.det(a))

# eigen values and eigen vectors
eigenvalues, eigenvectors = np.linalg.eig(a)
print("eigen values :", eigenvalues)
print("eigen vectors :\n", eigenvectors)

# singular value decomposition
U, S, Vt = np.linalg.svd(a)
print("SVD - U:\n", U)
print("SVD - S:", S)
print("SVD - Vt:\n", Vt)

# cholesky decomposition — needs a positive-definite matrix
pd_matrix = np.array([[4.0, 2.0], [2.0, 3.0]])
print("cholesky decomposition :\n", np.linalg.cholesky(pd_matrix))

# qr decomposition
Q, R = np.linalg.qr(a)
print("QR decomposition - Q:\n", Q)
print("QR decomposition - R:\n", R)

# LU decomposition (scipy)
P, L, U_mat = lu(a)
print("LU decomposition - P:\n", P)
print("LU decomposition - L:\n", L)
print("LU decomposition - U:\n", U_mat)

# rank of matrix
print("rank of matrix :", np.linalg.matrix_rank(a))

# trace of matrix
print("trace of matrix :", np.trace(a))

# condition number of matrix
print("condition number of matrix :", np.linalg.cond(a))

# matrix norm
print("matrix norm :", np.linalg.norm(a))

# matrix power
print("matrix power :\n", np.linalg.matrix_power(a.astype(int), 2))

# matrix exponential (scipy)
print("matrix exponential :\n", expm(a))

# matrix logarithm (scipy)
print("matrix logarithm :\n", logm(a))

# matrix square root (scipy)
print("matrix square root :\n", sqrtm(a))

# matrix inverse
print("matrix inverse :\n", np.linalg.inv(a))

# matrix pseudo inverse
print("matrix pseudo inverse :\n", np.linalg.pinv(a))

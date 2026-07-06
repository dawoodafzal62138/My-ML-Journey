import numpy as np
from operation import multiplication, transpose


def print_heading(title):
    print("\n" + "=" * 60)
    print(title.center(60))
    print("=" * 60)


def print_matrix(name, matrix):
    print(f"\n{name}:")
    print(matrix)


# ---------------- Matrix Multiplication ---------------- #

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([
    [7, 8],
    [9, 10],
    [11, 12]
])

print_heading("MATRIX MULTIPLICATION")

print_matrix("Matrix A", A)
print_matrix("Matrix B", B)

result = multiplication(A, B)

print("\nResult (A × B):")
print(result)

print("\nVerification using NumPy:")
print(np.matmul(A, B))

print("\nEqual to NumPy:", np.array_equal(result, np.matmul(A, B)))


# ---------------- Transpose ---------------- #

C = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print_heading("TRANSPOSE")

print_matrix("Original Matrix", C)

result = transpose(C)

print("\nTranspose:")
print(result)

print("\nVerification using NumPy:")
print(C.T)

print("\nEqual to NumPy:", np.array_equal(result, C.T))
import numpy as np
from numpy.typing import NDArray



def multiply_step_by_step(matrix1 : NDArray , matrix2: NDArray):
    if not isinstance(matrix1, np.ndarray) or not isinstance(matrix2, np.ndarray):
        return "Inputs must be NumPy arrays."
    if matrix1.size == 0 or matrix2.size == 0:
        return "Matrices cannot be empty."       
    if matrix1.ndim not in (1, 2) or matrix2.ndim not in (1, 2):
        return "Only 1D and 2D arrays are supported."


    if matrix1.ndim == 1:
        matrix1 = matrix1.reshape(1, -1)

    if matrix2.ndim == 1:
        matrix2 = matrix2.reshape(-1, 1)

    matrix1_row, matrix1_col = matrix1.shape
    matrix2_row, matrix2_col = matrix2.shape
   

    result = np.zeros((matrix1_row ,matrix2_col))
    for i in range(matrix1_row):
        for j in range(matrix2_col):
            total = 0
            for k in range(matrix1_col):
                total += matrix1[i, k] * matrix2[k, j]
            result[i, j] = total

    return  result








def transpose(matrix1 : NDArray):
    if not isinstance(matrix1, np.ndarray):
        return "Input must be NumPy array."
    if matrix1.size == 0:
        return "Matrix cannot be empty."       

    if matrix1.ndim not in (1, 2):
        return "Only 1D and 2D array is supported."



    if matrix1.ndim == 1:
        matrix1 = matrix1.reshape(1, -1)

    matrix1_row, matrix1_col = matrix1.shape
    result = np.zeros((matrix1_col , matrix1_row))
    for i in range(matrix1_row):
        for j in range(matrix1_col):
            result[j][i] = matrix1[i][j]
    
    
    return result



a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

print(transpose(a))



def inverse_step_by_step(matrix1 : NDArray , matrix2):
    pass


def get_determinent(matrix1 : NDArray , matrix2):
    pass

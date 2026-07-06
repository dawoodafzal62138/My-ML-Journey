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

    print(matrix1_row)  
    print(matrix1_col) 
    print(matrix2_row)
    print(matrix2_col)

    dict_row = {}
   
    for row_index in range(matrix1_row):
        dict_row[f"{row_index}_row"] = matrix1[row_index]
        cols = []
        for col_index in range(matrix2_col):
            cols.append(matrix2[ : ,col_index])
        dict_row[f"{row_index}_cols"] = cols



    return dict_row


a = np.array([[1,2,3]])
b = np.array([[7,8],
              [10,11],
              [13,14]])

print(multiply_step_by_step(a  ,b))














def inverse_step_by_step(matrix1 : NDArray , matrix2):
    pass

def transpose(matrix1 : NDArray , matrix2):
    pass

def get_determinent(matrix1 : NDArray , matrix2):
    pass

from numpy.typing import NDArray
import numpy as np



def one_hot_encoding_vectorized(labels_array: list, inputs: list) -> NDArray:
    labels = np.array(labels_array)
    inps = np.array(inputs)
    
    return (inps[: ,  np.newaxis] == labels).astype(int)


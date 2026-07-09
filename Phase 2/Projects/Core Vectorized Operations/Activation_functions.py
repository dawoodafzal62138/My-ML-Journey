from numpy.typing import NDArray
import numpy as np 



def sigmoid(x : NDArray) -> NDArray:

    return 1/(1+np.exp(-x))





# Rectified linear unit
def relu(x : NDArray) -> NDArray:
    return np.maximum(0 , x)



def softmax(x : NDArray) -> NDArray:
    shifted_x = x - np.max(x, axis=-1, keepdims=True)
    
    exps = np.exp(shifted_x)
    return exps / np.sum(exps, axis=-1, keepdims=True)


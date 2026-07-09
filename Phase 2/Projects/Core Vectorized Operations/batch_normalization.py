from numpy.typing import NDArray
import numpy as np


def batch_norm(x: NDArray , gamma: int , beta : int , epsilon :float = 1e-5):

    mean = np.mean(x , axis= 0, keepdims= True)

    var = np.var(x , axis= 0, keepdims= True)

    normalize = (x - mean) / np.sqrt(var + epsilon)

    y_i = (gamma * normalize) + beta 

    return y_i



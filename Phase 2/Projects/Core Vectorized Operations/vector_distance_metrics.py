from numpy.typing import NDArray
import numpy as np


def l2_distance(x : NDArray , y : NDArray) ->any:
    return np.sqrt(np.sum((x - y) ** 2))



def cosine_similarity(x : NDArray , y : NDArray) -> any:
    dot  =  np.dot(x , y)

    norm_x= np.linalg.norm(x)
    norm_y= np.linalg.norm(y)


    if norm_x == 0  or norm_y == 0:
        return 0.0
    
    return dot / (norm_x * norm_y)
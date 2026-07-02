import numpy as np 
from numpy.typing import NDArray

class Stats:


    def mean(self , array :NDArray ) -> float:
        return np.mean(array)

    def median(self , array : NDArray) -> float:
        return np.median(array)

    def mode(self , array : NDArray) -> float:
        a = np.bincount(array)
        return np.argmax(a)

    def std(self , array : NDArray ) -> float:
        return np.std(array)

    def variance(self , array : NDArray) -> float:
        return np.square(self.std(array))




rng = np.random.default_rng(seed= 1)
array = rng.integers(1,1000 ,10000)
# print(array)

s = Stats()


print(f"mean : {s.mean(array)}")
print(f" mode: {s.mode(array)}")
print(f"Standard deviation: {s.std(array)}")
print(f"median : {s.median(array)}")
print(f"Variance: {s.variance(array)}")
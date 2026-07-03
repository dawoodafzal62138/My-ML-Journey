import numpy
from numpy.typing import NDArray
from stats import *

stats = Stats()

class AdvanceStats:

    def covariance(self, array1 : NDArray , array2 : NDArray ) -> any:
        if len(array1) != len(array2) : 
            return "Both Arrays must be of same size"
        n = len(array1)
        numinator1 = array1 - stats.mean(array1)
        numinator2 = array2 - stats.mean(array2)
        numinator = np.sum(numinator1*numinator2)
        cov = float(numinator / n) 
        if cov > 0:
            return cov , "Positive Covariance"
        elif cov < 0:
            return cov , "Negative Covariance"
        else: 
            return cov , "Zero Covariance"

    def percentile_(self , array : NDArray , percentile: int) -> float:
        array = sorted(array)
        L = ((len(array) / 100) * percentile )
        print(L)
        if not L.is_integer():
            value = (array[int(L)-1] + array[int(L)]) / 2
        else:
            value = array[int(L) -1] 
        return value         

    def interquantile_range(self , array : NDArray) -> float:
        q75 = self.percentile_(array , 75)
        q25 = self.percentile_(array , 25)
        return q75 - q25

    def quartiles(self, array: NDArray) -> tuple:
        array = sorted(array)
        min_  = array[0]
        q1    = self.percentile_(array, 25)
        q2    = self.percentile_(array, 50)
        q3    = self.percentile_(array, 75)
        max_  = array[-1]
        return min_, q1, q2, q3, max_

    def min_max_normalization(self , array : NDArray) -> NDArray:
        return (array - np.min(array)) / (np.max(array) - np.min(array))

    def weighted_mean(self , array : NDArray , weights : NDArray) -> any:
        if len(array) != len(weights):
            return f"Both array and weights must be of same length"
    
        weighted_mean_ = np.sum((array * weights ))/ np.sum(weights)
        return weighted_mean_


x = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
y = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(x.ndim)
ads= AdvanceStats()
print(ads.weighted_mean(x , y))

import numpy
from numpy.typing import NDArray
from stats import *

stats = Stats()

class AdvanceStats:

    def population_covariance(self, array1 : NDArray , array2 : NDArray ) -> any:
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





x = [1, 2, 3, 4, 5]
y = [4, 1, 5, 2, 3]

ads= AdvanceStats()
print(ads.population_covariance(x , y))
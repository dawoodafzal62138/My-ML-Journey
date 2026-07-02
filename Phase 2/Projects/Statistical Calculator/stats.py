import numpy as np 
from numpy.typing import NDArray
import random
class Stats:


    def mean(self , array :NDArray ) -> float:
        return np.sum(array , dtype=np.float64) / len(array)

    def median(self , array : NDArray) -> float:
        return np.median(array)

    def mode(self , array : NDArray) -> float:
        values , count =  np.unique(array.astype(np.float64), return_counts=True)
        return values[np.argmax(count)]

    def std(self , array : NDArray ) -> float:
        return np.std(array , dtype= np.float64)

    def variance(self , array : NDArray) -> float:
        return np.square(self.std(array))

    def skewness(self , array : NDArray) -> tuple : 
        numinator = np.sum((array - self.mean(array))**3)
        denominator = (len(array)) * (self.std(array)**3)
        skew = np.round(float(numinator / denominator ) , 2)
        if skew > 0:
            return skew ,"Positively Skewed"
        elif skew < 0:
            return skew ,"Negatively Skewed"
        else:
            return skew , "Perfectly Balanced"


    def kurtosis(self , array : NDArray) -> tuple:
        numinator = np.sum((array - self.mean(array))**4)
        denominator = (len(array))*(self.std(array) ** 4)
        kur = np.round(float(numinator / denominator ) , 2)
        if kur > 3 :
            return kur , "Leptokurtic  - Heavy tails, sharp peak"
        elif kur < 3 :
            return kur , "Platykurtic  - Thin tails, flat peak"
        else:
            return kur , "Mesokurtic - Normal distribution"


    def confidence_interval(self , array : NDArray) -> tuple:
        # for confidence level 95%
        n = 30
        sample_array =  random.choices(array , k = n)
        z = 1.96
        sample_mean = self.mean(sample_array)
        sample_std = self.std(sample_array)
        margin = z * (sample_std / np.sqrt(n))
        return (sample_mean - margin, sample_mean + margin)








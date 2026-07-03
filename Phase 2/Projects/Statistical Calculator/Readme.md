# 📊 Statistical Calculator 

A lightweight yet powerful **Python statistics library** built from scratch using **NumPy**.

Statistical Calculator  provides essential descriptive statistics along with advanced statistical analysis utilities such as **covariance**, **percentiles**, **quartiles**, **interquartile range (IQR)**, **weighted mean**, **min-max normalization**, **distribution analysis**, and **95% confidence intervals**.

The project also includes a colorful terminal demonstration that evaluates the library on several probability distributions.

---

# ✨ Features

## 📈 Basic Statistics

- Mean
- Median
- Mode
- Population Variance
- Population Standard Deviation
- Sample Variance
- Sample Standard Deviation

## 📊 Distribution Analysis

- Skewness
- Kurtosis
- 95% Confidence Interval

## 📚 Advanced Statistics

- Covariance
- Percentiles
- Quartiles
- Interquartile Range (IQR)
- Weighted Mean
- Min-Max Normalization

## 🎨 Extras

- Beautiful terminal output with colors
- Tested on multiple probability distributions
- Easy-to-understand implementation
- Built entirely using NumPy

---

# 📂 Project Structure

```text
Statistical Calculator /
│
├── stats.py              # Core statistical functions
├── advance_stats.py      # Advanced statistical functions
├── main.py               # Demonstration script
└── README.md
```

---

# ⚙️ Installation


Install dependencies

```bash
pip install numpy
```

---

# 🚀 Quick Start

```python
import numpy as np

from stats import Stats
from advance_stats import AdvanceStats

stats = Stats()
adv = AdvanceStats()

data = np.array([10,20,30,40,50])
weights = np.array([1,2,3,4,5])

print(stats.mean(data))
print(stats.median(data))
print(stats.mode(data))
print(stats.variance(data))
print(stats.std(data))

print(stats.sample_variance_std(data))

print(stats.skewness(data))
print(stats.kurtosis(data))
print(stats.confidence_interval(data))

print(adv.covariance(data,data))
print(adv.percentile_(data,75))
print(adv.quartiles(data))
print(adv.interquantile_range(data))
print(adv.weighted_mean(data,weights))
print(adv.min_max_normalization(data))
```

---

# 📖 Available Functions

---

## Mean

Returns the arithmetic average.

```python
stats.mean(array)
```

Example

```python
>>> stats.mean(np.array([2,4,6,8]))
5.0
```

---

## Median

Returns the middle value.

```python
stats.median(array)
```

Example

```python
>>> stats.median(np.array([2,4,6,8]))
5.0
```

---

## Mode

Returns the most frequently occurring value.

```python
stats.mode(array)
```

Example

```python
>>> stats.mode(np.array([1,2,2,3]))
2
```

---

## Population Standard Deviation

Measures the spread of the data.

```python
stats.std(array)
```

Example

```python
>>> stats.std(np.array([1,2,3,4,5]))
1.4142
```

---

## Population Variance

Returns the variance of the dataset.

```python
stats.variance(array)
```

Example

```python
>>> stats.variance(np.array([1,2,3,4,5]))
2.0
```

---

## Sample Variance & Sample Standard Deviation

Randomly samples 30 observations and computes sample variance and sample standard deviation.

```python
stats.sample_variance_std(array)
```

Returns

```python
(sample_variance, sample_standard_deviation)
```

Example

```python
(2.35, 1.53)
```

---

## Skewness

Measures the symmetry of a distribution.

```python
stats.skewness(array)
```

Returns

```python
(skewness_value, description)
```

Possible descriptions

- Positively Skewed
- Negatively Skewed
- Perfectly Balanced

Example

```python
(0.87, "Positively Skewed")
```

---

## Kurtosis

Measures the heaviness of a distribution's tails.

```python
stats.kurtosis(array)
```

Returns

```python
(kurtosis_value, description)
```

Possible descriptions

- Leptokurtic
- Mesokurtic
- Platykurtic

Example

```python
(3.74, "Leptokurtic - Heavy tails, sharp peak")
```

---

## 95% Confidence Interval

Computes the confidence interval using a random sample of 30 observations.

```python
stats.confidence_interval(array)
```

Returns

```python
(lower_bound, upper_bound)
```

Example

```python
(12.54, 15.82)
```

---

# 📚 Advanced Statistics

---

## Covariance

Measures how two variables change together.

```python
adv.covariance(array1, array2)
```

Returns

```python
(covariance_value, relationship)
```

Possible relationships

- Positive Covariance
- Negative Covariance
- Zero Covariance

Example

```python
(5.81, "Positive Covariance")
```

---

## Percentile

Returns the specified percentile.

```python
adv.percentile_(array, percentile)
```

Example

```python
>>> adv.percentile_(data,75)
42.5
```

---

## Quartiles

Returns the five-number summary.

```python
adv.quartiles(array)
```

Returns

```python
(minimum, Q1, median, Q3, maximum)
```

Example

```python
(10,20,30,40,50)
```

---

## Interquartile Range (IQR)

Returns the spread of the middle 50% of the data.

```python
adv.interquantile_range(array)
```

Example

```python
20
```

---

## Weighted Mean

Computes the weighted average of observations.

```python
weights = np.array([1,2,3,4,5])

adv.weighted_mean(data,weights)
```

Example

```python
36.67
```

---

## Min-Max Normalization

Scales values between **0** and **1**.

```python
adv.min_max_normalization(array)
```

Example

```python
array([0.00,0.25,0.50,0.75,1.00])
```

---

# 🧪 Demonstration

Run

```bash
python main.py
```

The program automatically evaluates the library on multiple probability distributions.

Included distributions

- Normal Distribution
- Uniform Distribution
- Exponential Distribution
- Binomial Distribution
- Poisson Distribution
- Chi-Square Distribution
- Gamma Distribution
- Beta Distribution
- Log-Normal Distribution
- Triangular Distribution

For every distribution it calculates

- Mean
- Median
- Mode
- Variance
- Standard Deviation
- Sample Variance
- Sample Standard Deviation
- Skewness
- Kurtosis
- Confidence Interval
- Covariance
- Percentiles
- Quartiles
- Interquartile Range
- Weighted Mean
- Min-Max Normalization

---

# 📦 Requirements

- Python 3.10+
- NumPy

Install dependencies

```bash
pip install numpy
```

---




# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Dawood Afzal**

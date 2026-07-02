# 📊 Statistical Calculator

A lightweight Python statistics library built from scratch using **NumPy**.  
PyStats provides common descriptive statistical functions along with distribution analysis utilities such as **skewness**, **kurtosis**, and **95% confidence intervals**.

The project also includes a colorful terminal demo that evaluates the library on several probability distributions.

---

## ✨ Features

- 📈 Mean
- 📊 Median
- 📌 Mode
- 📉 Standard Deviation
- 📐 Variance
- ↗️ Skewness Detection
- 🔔 Kurtosis Detection
- 🎯 95% Confidence Interval
- 🎨 Beautiful colored terminal output
- 🧪 Tested on multiple probability distributions

---

## Project Structure

```
PyStats/
│
├── stats.py        # Statistics library
├── main.py         # Demonstration script
└── README.md
```

---

## Installation



Install dependencies

```bash
pip install numpy
```

---

## Quick Start

```python
import numpy as np
from stats import Stats

stats = Stats()

data = np.array([10, 15, 18, 20, 25])

print(stats.mean(data))
print(stats.median(data))
print(stats.mode(data))
print(stats.std(data))
print(stats.variance(data))
print(stats.skewness(data))
print(stats.kurtosis(data))
print(stats.confidence_interval(data))
```

---

# Available Functions

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

## Standard Deviation

Measures how spread out the data is.

```python
stats.std(array)
```

---

## Variance

Returns the variance of the dataset.

```python
stats.variance(array)
```

---

## Skewness

Measures the symmetry of a distribution.

```python
stats.skewness(array)
```

Returns

```python
(skew_value, description)
```

Possible descriptions

- Positively Skewed
- Negatively Skewed
- Perfectly Balanced

Example

```python
(1.25, "Positively Skewed")
```

---

## Kurtosis

Measures the heaviness of the tails.

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
(4.12, "Leptokurtic - Heavy tails, sharp peak")
```

---

## Confidence Interval

Computes a **95% confidence interval** from a random sample of 30 observations.

```python
stats.confidence_interval(array)
```

Returns

```python
(lower_bound, upper_bound)
```

Example

```python
(12.45, 15.87)
```

---

# Demonstration

Running

```bash
python main.py
```

tests the library on several probability distributions.

Included distributions

- Normal
- Uniform
- Exponential
- Binomial
- Poisson
- Chi-Square
- Gamma
- Beta
- Log-Normal
- Triangular

Example output

```
================================================================================
                         STATISTICAL FUNCTIONS TEST
================================================================================

                         Normal Distribution
--------------------------------------------------------------------------------
Mean                :     0.0193
Median              :     0.0253
Mode                :    -3.2413
Standard Deviation  :     0.9787
Variance            :     0.9578
Skewness            :      0.12 (Positively Skewed)
Kurtosis            :      2.96 (Platykurtic)
95% Confidence Int. : [-0.3514, 0.3768]
```

---

# Requirements

- Python 3.10+
- NumPy

Install

```bash
pip install numpy
```

---

# Future Improvements

- Sample variance
- Sample standard deviation
- Covariance
- Correlation coefficient
- Percentiles
- Quartiles
- Interquartile Range (IQR)
- Z-score
- Min-Max normalization
- Robust mode implementation
- Weighted mean
- Bootstrap confidence intervals
- Hypothesis testing
- Linear regression utilities
- Visualization using Matplotlib
- Unit tests with pytest

---



# License

This project is licensed under the MIT License.

---

## Author

**Dawood Afzal**

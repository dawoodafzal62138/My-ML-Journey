# Monte Carlo Pi Estimator

Estimate the value of **π (Pi)** using the **Monte Carlo method** and **NumPy vectorization**. This project demonstrates how random sampling can be used to approximate mathematical constants while introducing the fundamentals of probability, geometry, and numerical simulation.

---

## Project Overview

The Monte Carlo method is a statistical technique that estimates numerical values using random sampling. In this project, millions of random points are generated inside a square. By determining how many of these points fall inside an inscribed circle, the value of π is approximated using the ratio of their areas.

The implementation is fully vectorized with **NumPy**, allowing efficient computation without explicit Python loops.

---

## Mathematical Background

Consider a circle of radius **r** perfectly inscribed inside a square.

### Area of the Circle

$$
A_{circle}=\pi r^2
$$

### Area of the Square

$$
A_{square}=(2r)^2=4r^2
$$

Taking the ratio of the two areas,

$$
\frac{A_{circle}}{A_{square}}
=
\frac{\pi r^2}{4r^2}
=
\frac{\pi}{4}
$$

If random points are uniformly distributed throughout the square, then

$$
\frac{\text{Points Inside Circle}}
{\text{Total Points}}
\approx
\frac{\pi}{4}
$$

Therefore,

$$
\boxed{\pi \approx 4\frac{I}{N}}
$$

where

- **I** = Number of points inside the circle
- **N** = Total number of randomly generated points

---


## Project Workflow

1. Create a square with an inscribed circle.
2. Generate **N** uniformly distributed random points inside the square.
3. Determine whether each point satisfies

   $$
   x^2+y^2\le r^2
   $$

4. Count the number of points inside the circle.
5. Estimate π using

   $$
   \pi \approx 4\frac{I}{N}
   $$

6. Visualize the simulation.

---

## Project Structure

```
Monte_Carlo_Pi_Estimator/
│
├── main.ipynb          # Complete implementation and explanation
└── README.md           # Project documentation
```

---

## Requirements

- Python 3.10+
- NumPy
- Matplotlib

Install the required libraries using:

```bash
pip install numpy matplotlib
```

---

## Example Output

```
Actual Pi     : 3.141592653589793
Estimated Pi  : 3.140968
Absolute Error: 0.000625
```

> Since the algorithm relies on random sampling, the estimated value changes slightly on each execution unless a fixed random seed is used.



## Error Analysis

The Monte Carlo estimator converges according to

$$
\boxed{\text{Error}\propto\frac{1}{\sqrt{N}}}
$$

where **N** is the number of random samples.

This means:

- Increasing the number of samples improves the estimate.
- The improvement is gradual rather than linear.
- To reduce the error by a factor of **10**, approximately **100 times** more samples are required.

As

$$
N\rightarrow\infty,
$$

the estimate converges toward the true value of π according to the **Law of Large Numbers**.



---

# License

This project is released under the **MIT License**.

---

# Author

**Dawood Afzal**
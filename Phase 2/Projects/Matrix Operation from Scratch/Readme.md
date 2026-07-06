# Matrix Operations from Scratch using NumPy

A beginner-friendly implementation of fundamental matrix operations **from scratch** using only **NumPy arrays** and Python loops. The goal of this project is to understand the mathematics behind matrix operations rather than relying on built-in NumPy functions such as `np.matmul()`, `np.transpose()`.

---

# Project Objective

The purpose of this project is to implement the core matrix operations manually and build a strong understanding of linear algebra algorithms.

Every operation is implemented using:

- Python loops
- NumPy arrays for storage
- Basic arithmetic operations
- Matrix indexing

The implementation avoids using NumPy's built-in matrix operation functions.

---

# Features

Currently implemented operations:

- Matrix Multiplication
- Matrix Transpose

Planned operations:

- Add Graphs to visualize , after i learn matplotlib

---

# Technologies Used

- Python 3.x
- NumPy

---

# Project Structure

```
Matrix-Operations/
│
├── operation.py          # Matrix algorithms
├── main.py               # Terminal main script
└README.md

```

---



# Example Usage

```python
import numpy as np
from operation import multiplication, transpose

A = np.array([
    [1,2,3],
    [4,5,6]
])

B = np.array([
    [7,8],
    [9,10],
    [11,12]
])

print(multiplication(A,B))
```

Output

```
[[ 58.  64.]
 [139. 154.]]
```

Transpose

```python
print(transpose(A))
```

Output

```
[[1. 4.]
 [2. 5.]
 [3. 6.]]
```

---


# Author

**DAWOOD AFZAL**

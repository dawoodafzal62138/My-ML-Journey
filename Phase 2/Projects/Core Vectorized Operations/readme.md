# Core Vectorization Operations

 A beginner-friendly implementation of essential Machine Learning operations using **NumPy** only



The project covers:

- Activation Functions
- Distance Metrics
- One-Hot Encoding
- Batch Normalization

Each implementation is fully vectorized using NumPy for efficiency and readability.

---

## 📂 Project Structure

```
.
│
├── Activation_functions.py        # Sigmoid, ReLU, Softmax
├── vector_distance_metrics.py     # Cosine Similarity & L2 Distance
├── one_hot_encoding.py            # One-Hot Encoding
├── batch_normalization.py         # Batch Normalization
├── main.ipynb                     # Demonstrations and examples
└── README.md
```

---

# 🚀 Features

## ✅ Activation Functions

Implements the most common neural network activation functions.

- Sigmoid
- ReLU (Rectified Linear Unit)
- Softmax

These functions introduce non-linearity into neural networks and are responsible for learning complex relationships.

---

## ✅ Distance Metrics

Implements commonly used similarity and distance measures.

- Euclidean (L2) Distance
- Cosine Similarity

Useful in:

- Recommendation Systems
- NLP
- Image Retrieval
- Clustering
- Similarity Search

---

## ✅ One-Hot Encoding

Converts categorical labels into binary vectors.

Example:

| Label | One-Hot |
|-------|---------|
| Cat | [1,0,0] |
| Dog | [0,1,0] |
| Bird | [0,0,1] |

Used in:

- Classification
- Neural Networks
- NLP
- Data Preprocessing

---

## ✅ Batch Normalization

Normalizes each feature across a mini-batch.

Benefits:

- Faster convergence
- Stable gradients
- Reduced internal covariate shift
- Allows higher learning rates

---

# 📚 Concepts Covered

## 1. Sigmoid Function

### Formula


$$sigma(x)=\frac{1}{1+e^{-x}}
$$

Range:

```
0 → 1
```

Commonly used for:

- Binary Classification
- Logistic Regression

---

## 2. ReLU

### Formula


$$ReLU(x)=max(0,x)$$


Range

```
0 → +∞
```

Advantages

- Fast
- Simple
- Prevents vanishing gradients

Most widely used activation in deep learning.

---

## 3. Softmax

### Formula


$$Softmax(x_i)=\frac{e^{x_i}}{\sum_j e^{x_j}}$$


Converts scores into probabilities.

Properties

- Output sums to 1
- Used for multi-class classification

---

## 4. Euclidean (L2) Distance

### Formula


$$d(x,y)=\sqrt{\sum_{i=1}^{n}(x_i-y_i)^2}$$


Measures the straight-line distance between two vectors.

Applications

- KNN
- Clustering
- Computer Vision

---

## 5. Cosine Similarity

### Formula


$$Cos(x,y)=\frac{x \cdot y}{||x||\,||y||}
$$

Measures the angle between vectors rather than their magnitude.

Range

```
-1 → 1
```

Applications

- Search Engines
- Recommendation Systems
- NLP
- Sentence Embeddings

---

## 6. One-Hot Encoding

Transforms categorical values into binary vectors.

Example

```
Labels

Cat
Dog
Bird

↓

Encoded

Cat  -> [1 0 0]
Dog  -> [0 1 0]
Bird -> [0 0 1]
```

---

## 7. Batch Normalization

Batch Normalization standardizes inputs using the batch mean and variance.

### Step 1

Calculate mean

$$
\mu=\frac{1}{m}\sum x_i
$$

### Step 2

Calculate variance

$$
\sigma^2=\frac{1}{m}\sum(x_i-\mu)^2
$$

### Step 3

Normalize

$$
\hat{x}=\frac{x-\mu}{\sqrt{\sigma^2+\epsilon}}
$$

### Step 4

Scale and Shift

$$
y=\gamma\hat{x}+\beta
$$

Where

- γ (gamma) = scale
- β (beta) = shift

---

# 🛠 Technologies Used

- Python 3.x
- NumPy
- Jupyter Notebook

---

# 📦 Installation


Install dependencies

```bash
pip install numpy
```


# ▶️ Running the Project

Run the notebook

```bash
jupyter notebook main.ipynb
```

or execute the individual Python files.

---

# 📁 Module Description

## Activation_functions.py

Contains implementations of

- Sigmoid
- ReLU
- Softmax

---

## vector_distance_metrics.py

Contains

- Euclidean (L2) Distance
- Cosine Similarity

---

## one_hot_encoding.py

Contains a vectorized implementation of One-Hot Encoding using NumPy broadcasting.

---

## batch_normalization.py

Implements Batch Normalization from scratch using

- Mean
- Variance
- Standardization
- Scaling
- Shifting

---

## main.ipynb

Contains demonstrations and examples for all implemented algorithms.

---



# 📈 Applications

These implementations are fundamental building blocks used in

- Deep Learning
- Computer Vision
- Natural Language Processing
- Recommendation Systems
- Classification
- Clustering
- Feature Engineering

---


# 📜 License

This project is released under the MIT License.

---

# 👨‍💻 Author

**Dawood Afzal**

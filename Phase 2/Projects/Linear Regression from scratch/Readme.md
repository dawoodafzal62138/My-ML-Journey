# Linear Regression from Scratch

A pure NumPy implementation of linear regression — no sklearn, no shortcuts. Built to understand what happens under the hood when a machine learning library fits a line to data.

---

## Project Structure

```
├── LR_one_feature.ipynb       # Single feature: house size → price
├── LR_many_feature.ipynb      # Multiple features: size + bedrooms + bathrooms + floors → price
├── data.csv                   # 100-row synthetic dataset (house_size, price)
└── data2.csv                  # Extended dataset with 7 features
```

---

## What This Project Covers

**Notebook 1 — One Feature**
Predicts house price from house size alone using `ŷ = wx + b`. Covers the full gradient descent loop from scratch, convergence detection, and denormalization of predictions back to real dollar values.

**Notebook 2 — Multiple Features**
Extends the model to four features: `ŷ = w₁(size) + w₂(bedrooms) + w₃(bathrooms) + w₄(floors) + b`. Includes visual feature analysis to identify and drop features with no correlation to price before training.

---

## Dataset

`data.csv` — 100 synthetic houses with size (sq ft) and price ($).

`data2.csv` — Same 100 houses extended with 7 features:

| Feature | Description |
|---|---|
| house_size | Square footage (500–3500) |
| price | Sale price in USD |
| bedrooms | Number of bedrooms (1–6) |
| bathrooms | Number of bathrooms (1–4) |
| floors | Number of floors (1–3) |
| garage | Has garage (0 or 1) |
| age | Years since built |
| distance_to_city_km | Distance to city center (km) |

After visual analysis, `age` and `distance_to_city_km` showed no correlation with price and were dropped before training.

---

## Why No sklearn

sklearn's `LinearRegression` calls a matrix solver internally and hands back coefficients. This project computes every step manually — the cost, the gradient, the weight update — to build a real understanding of what the library is abstracting away.

---

## Requirements

```
numpy
pandas
matplotlib
```

Install with:
```bash
pip install numpy pandas matplotlib
```

---

## Results

| Model | Features | MAE |
|---|---|---|
| Single feature | house_size | ~$24,000 |
| Multiple features | size + bedrooms + bathrooms + floors | ~$24500 |

Both models trained using gradient descent with convergence stopping (loop exits when cost change < `1e-10`).




---
# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Dawood Afzal**
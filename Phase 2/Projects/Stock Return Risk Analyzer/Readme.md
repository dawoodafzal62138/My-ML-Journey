# 📈 Stock Return Risk Analyzer

A beginner-friendly **NumPy ** project that analyzes the historical performance of multiple stocks using fundamental concepts from quantitative finance.



# Features

- Download historical stock prices using Yahoo Finance
- Calculate daily percentage returns
- Compute annualized returns
- Measure annualized risk (volatility)
- Calculate Sharpe Ratio
- Generate covariance matrix
- Estimate portfolio risk
- Visualize financial metrics with charts

---

# Technologies Used

- Python
- NumPy
- Matplotlib
- yfinance

---

# Project Structure

```
Stock-Return-Risk-Analyzer/
│
├── main.ipynb
├── README.md
```

---

# Dataset


Historical stock prices are downloaded directly from **Yahoo Finance** using the `yfinance` library.

Example companies used:

- Microsoft (MSFT)
- Google (GOOG)
- Amazon (AMZN)

---

# Workflow

The notebook performs the following steps:

1. Download historical stock prices.
2. Extract adjusted closing prices.
3. Compute daily percentage returns.
4. Calculate annual returns.
5. Measure annual risk (volatility).
6. Compare stocks using the Sharpe Ratio.
7. Build the covariance matrix.
8. Calculate the risk of an equally weighted portfolio.
9. Visualize results using bar charts and heatmaps.

---

# Visualizations

The notebook includes multiple visualizations, including:

- Annual Return comparison
- Annual Risk comparison
- Sharpe Ratio comparison
- Covariance Matrix heatmap

These plots make it easier to compare the performance and risk characteristics of each stock.

---

# Financial Metrics Implemented

- Daily Return
- Annual Return
- Annual Risk (Volatility)
- Sharpe Ratio
- Covariance Matrix
- Portfolio Risk


---

# Requirements

Install the required packages:

```bash
pip install numpy  matplotlib yfinance
```

---

# How to Run


Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open the notebook and run all cells.

---

# Example Output

The notebook produces:

- Daily returns for each stock
- Annual return values
- Annual volatility values
- Sharpe Ratio comparison
- Covariance matrix
- Portfolio risk
- Multiple comparison charts


# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Dawood Afzal**

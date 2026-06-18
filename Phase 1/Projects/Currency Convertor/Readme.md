# 💱 Currency Converter

A terminal-based currency converter built in Python that fetches real-time exchange rates using the [ExchangeRate-API](https://www.exchangerate-api.com/).

---

## ✨ Features

- 🌍 View all supported currency codes with full names
- 🔄 Convert any currency to another in real-time
- 💅 Clean, colorful terminal UI with ANSI styling
- ⏳ Spinner animation while fetching data
- ✅ Input validation and graceful error handling

---

## 📋 Requirements

- Python 3.7+
- `requests`
- `halo`

Install dependencies with:

```bash
pip install requests halo
```

---

## 🔑 Getting Your API Key

1. Go to **[https://www.exchangerate-api.com/](https://www.exchangerate-api.com/)**
2. Click **"Get Free Key"** and sign up for a free account
3. After signing in, your **API key** will be shown on the dashboard
4. Copy the API key

---

## ⚙️ Configuration

Open `main.py` and paste your API key at **line 126**:

```python
# Line 126 — replace "Your-API-Key" with your actual key
API_KEY = "Your-API-Key"   # <-- paste here
```

It should look like this after pasting:

```python
API_KEY = "abc123xyz789yourkeyhere"
```

---

## 🚀 Usage

Run the script from your terminal:

```bash
python currency_converter.py
```

You'll be greeted with a menu:

```
------------------------------------------
  CURRENCY CONVERTER MENU
------------------------------------------
  [1]  View Supported Currencies
  [2]  Convert Currency
  [3]  Exit
------------------------------------------
```

### Option 1 — View Supported Currencies
Displays all available currency codes and their full names in a formatted grid.

### Option 2 — Convert Currency
Prompts you to enter:
- Source currency code (e.g. `USD`)
- Target currency code (e.g. `PKR`)
- Amount to convert

Then displays the exchange rate and converted amount.

---

## 📁 Project Structure

```
currency_converter/
│
├──   main.py     # Main script
└──   Readme.md   # Instructions

```

---

## 🛠️ Error Handling

The app gracefully handles:

| Error | Message Shown |
|---|---|
| Invalid API Key | `Error: invalid-key` |
| No internet connection | `Error: Cannot connect to server` |
| Invalid currency code | API error message displayed |
| Non-numeric amount input | `Invalid Input!` |
| Negative amount | `Amount Can't be Negative` |

---

## 📌 Notes

- The free plan of ExchangeRate-API allows **1,500 requests/month**
- Currency codes follow the **ISO 4217** standard (e.g. `USD`, `EUR`, `PKR`)
- Works on both **Windows** and **Linux/macOS**

---

## 📄 License

This project is open-source and free to use.
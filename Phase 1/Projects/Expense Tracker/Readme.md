# 💰 Expense Tracker

A modern, easy-to-use desktop application built with Python and **CustomTkinter** that helps you track your daily income and expenses, calculate your net balance, and view your financial history.

## ✨ Features

* **Interactive Dashboard**: Get a quick overview of your Total Income, Total Expenses, and Net Balance on responsive, color-coded summary cards.
* **Add Transactions**: Easily record your incomes and expenses with a user-friendly form.
* **Interactive Date Picker**: Choose dates visually using a built-in calendar popup (`tkcalendar`).
* **Categorization**: Pre-defined categories for both incomes (Salary, Freelance, etc.) and expenses (Food, Rent, Utilities, etc.).
* **History Log**: View all your past transactions in a clean table format. Filter your history by "All", "Income", or "Expenses".
* **Dark/Light Mode**: Toggle between a sleek dark theme and a bright light theme with the click of a switch.
* **Local Storage**: All data is securely stored on your local machine in a simple `expenses.csv` file.

## 🛠️ Tech Stack & Dependencies

This project is written in **Python 3** and utilizes the following libraries:

* `customtkinter` (For the modern GUI)
* `tkcalendar` (For the date selection popup)[cite: 1]
* `CTkMessagebox` (For modern alert and success popups)[cite: 1]
* `CTkTable` (For rendering the history data table)[cite: 1]

## 🚀 Installation & Setup

1. **Clone or Download the Repository:**
   Ensure you have all the project files (`GUI.py` and `main.py`) in the same folder.

2. **Install Required Libraries:**
   Open your terminal or command prompt and run the following command to install the required dependencies:
```bash
   pip install customtkinter tkcalendar CTkMessagebox CTkTable
```

3. **Run the Application:**
Start the application by running the `GUI.py` file:
```Bash
python GUI.py
```

## 🎮 How to Use
1. **Dashboard Tab:** View your current financial standing. Click the refresh button to update your totals after adding new data.

2. **Add Expense/Income Tab:** Select whether the entry is an Income or Expense, enter the amount, select a category from the dropdown, choose a date from the calendar, and add an optional description. Click Save! to log the transaction.

3. **History Tab:** View a complete breakdown of where your money is going. Use the segmented button at the top to filter between All entries, Income, or Expenses.

4. **Theme Toggle**: Use the switch in the top right corner to flip the app between Dark Mode and Light Mode.

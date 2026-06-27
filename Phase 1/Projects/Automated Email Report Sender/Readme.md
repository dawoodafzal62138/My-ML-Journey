# 📊 Daily Sales Report — AI Email Automation

A Python automation tool that reads sales data from a CSV file, analyzes it using **Google Gemini AI**, and emails the generated report directly to a recipient via Gmail.

---

## 📁 Project Structure

```
project/
├── main.py                          # Main script
├── prompt.txt                       # System prompt for Gemini AI
├── Online Sales Data kaggle.csv     # Your sales data CSV file
├── example.env                      # Template — copy this and rename to .env
└── README.md
```

---

## ⚙️ How It Works

1. **Reads** the CSV file and filters columns: `Product Category`, `Units Sold`, `Unit Price`, `Total Revenue`, `Region` (first 32 rows).
2. **Sorts** the data by `Product Category` then `Region`.
3. **Sends** the data to Gemini AI along with a custom system prompt from `prompt.txt`.
4. **Emails** the AI-generated analysis to the configured recipient via Gmail SMTP.

---

## 📦 Installation





### 1. Install required libraries

```bash
pip install google-genai python-dotenv
```

| Library | Purpose |
|---|---|
| `google-genai` | Google Gemini AI client |
| `python-dotenv` | Load environment variables from `.env` |
| `csv`, `pathlib`, `smtplib`, `email` | Built-in Python — no installation needed |

---

## 🔑 Environment Variables Setup



Copy the example file and fill in your keys:

```bash
cp example.env .env
```


---

### 🔷 Getting Your Gemini API Key

1. Go to [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account.
3. Click **"Create API Key"**.
4. Copy the generated key and paste it as the value of `GEMINI_API` in your `.env` file.

```
GEMINI_API=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

---

### 🔷 Getting Your Gmail App Password

A Gmail **App Password** is a 16-character code that lets your script send emails without exposing your real Gmail password.

**Prerequisites:** Your Gmail account must have **2-Step Verification enabled**.

**Steps:**

1. Go to your Google Account: [https://myaccount.google.com](https://myaccount.google.com)
2. Click **"Security"** in the left sidebar.
3. Under *"How you sign in to Google"*, click **"2-Step Verification"** and ensure it is turned **ON**.
4. In the search bar at the top of your account page, search for **"App Passwords"**.
5. Click on **App Passwords**.
6. Under *"App name"*, type a name like `Sales Report Script` and click **"Create"**.
7. Google will show you a **16-character password** — copy it immediately (it won't be shown again).
8. Paste it as the value of `APP_PASSWORD` in your `.env` file:

```
APP_PASSWORD=abcd efgh ijkl mnop
```

> You can include or exclude the spaces — both work.

---

## 📧 Configuring Email Addresses

Open `main.py` and update the two email addresses inside the `send_email()` function:

```python
# Line ~81 — the Gmail account you are sending FROM
sender_email = "your_gmail_address@gmail.com"

# Line ~86 — the email address you want to receive the report
receiver_email = "recipient_address@gmail.com"
```

> The `sender_email` must be the same Gmail account whose App Password you generated above.
> The `receiver_email` can be any valid email address.

---

## 📝 Customizing the AI Prompt

Edit `prompt.txt` to control how Gemini analyzes your data. For example:

```
You are a business analyst. Analyze the sales data provided and give:
1. A brief summary of total revenue by region.
2. The top-performing product category.
3. Any notable trends or anomalies.
Keep the response concise and suitable for an executive email.
```

If `prompt.txt` is missing or empty, the AI will analyze the data without any special instructions.

---

## ▶️ Running the Script

```bash
python main.py
```

**Expected output:**

```
Connecting to server...
Login successful!
Email sent successfully!
```

---

## 🕐 Scheduling with Windows Task Scheduler

You can automate this script to run daily (or at any interval) without opening a terminal manually.

---

### Step 1 — Find Your Python Executable Path

Task Scheduler needs the **full absolute path** to `python.exe`. If you are using a virtual environment (recommended), use that path, not the system Python.

Open a terminal inside your project folder with the venv activated and run:

```bash
where python
```

Copy the path that points inside your project's `venv` folder. It will look like:

```
C:\Users\YourName\projects\sales-report\venv\Scripts\python.exe
```

> If you are **not** using a venv, the path will look like:
> `C:\Users\YourName\AppData\Local\Programs\Python\Python311\python.exe`

---

### Step 2 — Create a Batch File (Recommended)

Using a `.bat` file makes Task Scheduler easier to configure and debug.

Create a new file called `run.bat` in your project folder with this content:

```bat
@echo off
cd /d "C:\Users\YourName\projects\sales-report"
"C:\Users\YourName\projects\sales-report\venv\Scripts\python.exe" main.py
```

> Replace both paths with your actual project folder path and Python path from Step 1.

Test it by double-clicking `run.bat` — you should see the script execute in a command window.

---

### Step 3 — Open Task Scheduler

1. Press `Win + S` and search for **"Task Scheduler"**.
2. Click on **Task Scheduler** to open it.

---

### Step 4 — Create a New Task

1. In the right-hand **Actions** panel, click **"Create Basic Task..."**
2. **Name:** `Daily Sales Report`
3. **Description:** `Runs the AI sales report script and sends an email.`
4. Click **Next**.

---

### Step 5 — Set the Trigger (Schedule)

1. Select **"Daily"** and click **Next**.
2. Set the **Start date** to today.
3. Set the **time** you want the report to be sent — for example `08:00:00 AM`.
4. Recur every `1` day.
5. Click **Next**.

---

### Step 6 — Set the Action

1. Select **"Start a program"** and click **Next**.
2. Fill in the fields:

| Field | Value |
|---|---|
| **Program/script** | Full path to your `run.bat` file, e.g. `C:\Users\YourName\projects\sales-report\run.bat` |
| **Add arguments** | Leave blank (the `.bat` handles everything) |
| **Start in** | Your project folder, e.g. `C:\Users\YourName\projects\sales-report` |

3. Click **Next**, then **Finish**.

---

### Step 7 — Configure Advanced Settings

After creating the task, right-click it in the Task Scheduler library and select **"Properties"** to configure important options:

**General tab:**
- Check **"Run whether user is logged on or not"** — this ensures the task runs even if you are away from the computer.
- Check **"Run with highest privileges"** if you encounter permission errors.

**Conditions tab:**
- Uncheck **"Start the task only if the computer is on AC power"** if you are on a laptop and want it to run on battery too.

**Settings tab:**
- Check **"If the task fails, restart every"** → set to `5 minutes`, up to `3 times` — this handles temporary network issues.
- Set **"Stop the task if it runs longer than"** → `30 minutes` as a safety limit.

Click **OK** and enter your Windows login password when prompted.

---

### Step 8 — Test the Task

Right-click your task in the Task Scheduler library and click **"Run"**. Then check:
- Your recipient inbox for the email.
- The **History tab** of the task for status codes (value `0` = success).

---

### Task Scheduler Troubleshooting

| Problem | Likely Cause | Fix |
|---|---|---|
| Task shows "Last Run Result: 0x1" | Script crashed | Run `run.bat` manually to see the actual error |
| Task runs but no email arrives | Wrong Python path in `.bat` | Confirm the venv Python path with `where python` |
| Task does not run at scheduled time | PC was off or sleeping | Enable **"Run task as soon as possible after a scheduled start is missed"** in Settings tab |
| "Access denied" error | Insufficient privileges | Enable **"Run with highest privileges"** in General tab |
| `.env` file not found | Wrong working directory | Confirm **Start in** is set to the exact project folder |

---

## 🛠️ Troubleshooting

| Problem | Likely Cause | Fix |
|---|---|---|
| `ClientError` from Gemini | Invalid or missing API key | Double-check `GEMINI_API` in `.env` |
| `SMTPAuthenticationError` | Wrong App Password or 2FA not enabled | Re-generate App Password; ensure 2FA is on |
| `FileNotFoundError` | CSV file path is wrong | Confirm the CSV file name matches exactly in `main.py` |
| Email sends but body is empty | `prompt.txt` missing | Create the file, even if blank |
| `ModuleNotFoundError` | Libraries not installed | Run `pip install google-genai python-dotenv` |

---



## 📋 Requirements Summary

| Requirement | Value |
|---|---|
| Python version | 3.8 or higher |
| Gemini model used | `gemini-3.1-flash-lite` |
| Gmail security requirement | 2-Step Verification must be enabled |
| SMTP Server | `smtp.gmail.com` port `587` |
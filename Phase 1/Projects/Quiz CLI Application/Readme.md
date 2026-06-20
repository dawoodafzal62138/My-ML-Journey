# 🧠 Quiz App — Learn. Play. Improve.

```
 ██████╗ ██╗   ██╗██╗███████╗     █████╗ ██████╗ ██████╗ 
██╔═══██╗██║   ██║██║╚══███╔╝    ██╔══██╗██╔══██╗██╔══██╗
██║   ██║██║   ██║██║  ███╔╝     ███████║██████╔╝██████╔╝
██║▄▄ ██║██║   ██║██║ ███╔╝      ██╔══██║██╔═══╝ ██╔═══╝ 
╚██████╔╝╚██████╔╝██║███████╗    ██║  ██║██║     ██║     
 ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝     ╚═╝     
```

A colorful, AI-powered terminal quiz app built with Python and Google Gemini. Test your knowledge across 15 subjects at 3 difficulty levels — all from your command line.

---

## ✨ Features

- 🤖 AI-generated questions via **Gemini 3.1 Flash-Lite**
- 🎨 Colorful terminal UI with ANSI color codes
- 📚 15 subjects — from Science to Art & Culture
- 🎯 3 difficulty levels — Easy, Medium, Hard
- 📜 Persistent quiz history saved to `history.txt`
- ⏳ Loading spinner while AI generates questions

---

## 📋 Requirements

- Python 3.8+
- A Google Gemini API key (free tier available)

---

## 🚀 Setup & Installation



### 1. Install required libraries

```bash
pip install google-genai python-dotenv halo
```


### 2. Get your Gemini API Key

1. Go to [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy the generated key

### 4. Set up your `.env` file

An `example.env` file is included in the project. Copy it to `.env`:

**On Linux / macOS:**
```bash
cp example.env .env
```

**On Windows:**
```cmd
copy example.env .env
```

Now open `.env` and paste your API key:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Running the App

```bash
python main.py
```

---

## 🗂️ Project Structure

```
quiz-app/
│
├── main.py          # Main application
├── prompt.txt       # System prompt for Gemini
├── example.env      # Environment variable template
├── .env             # Your API key (create from example env)
├── history.txt      # Auto-created after first quiz
└── README.md
```

---

## 🎮 How to Use

1. Run the app with `python main.py`
2. From the main menu, choose:
   - `[1]` Start Quiz
   - `[2]` See History
   - `[3]` Exit
3. Select a **subject** from the list (e.g. Science, History, Sports)
4. Select a **difficulty** — Hard, Medium, or Easy
5. Answer 10 AI-generated questions by entering the option number
6. See your score at the end — results are saved to `history.txt`

---

## 📚 Available Subjects

| # | Subject           |
|---|-------------------|
| 1 | General Knowledge |
| 2 | Science           |
| 3 | Mathematics       |
| 4 | History           |
| 5 | Geography         |
| 6 | Technology        |
| 7 | Sports            |
| 8 | Entertainment     |
| 9 | Literature        |
|10 | Business          |
|11 | Health            |
|12 | Nature            |
|13 | Politics          |
|14 | Art & Culture     |
|15 | Mixed Quiz        |

---

## 🌈 Terminal Color Support

This app uses **ANSI escape codes** for colors. These display correctly in:

- ✅ Linux & macOS terminals (native support)
- ✅ Windows Terminal
- ✅ VS Code integrated terminal
- ✅ PowerShell (Windows 10+)
- ❌ Old Windows CMD (may show raw codes like `←[32m`)

If you're on older Windows CMD and colors don't render, switch to **Windows Terminal** or run:
```cmd
reg add HKCU\Console /v VirtualTerminalLevel /t REG_DWORD /d 1
```




---

## 📄 License

MIT License — free to use, modify, and distribute.
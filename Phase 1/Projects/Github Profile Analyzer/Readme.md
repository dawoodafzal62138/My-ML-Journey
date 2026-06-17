# GitHub Profile Analyzer

A terminal-based tool that fetches GitHub profile data and generates an AI-powered career analysis report using Google Gemini.

```
 _____ _ _   _   _       _      ______           __ _ _         ___              _                    
|  __ (_) | | | | |     | |     | ___ \         / _(_) |       / _ \            | |                   
| |  \/_| |_| |_| |_   _| |__   | |_/ / __ ___ | |_ _| | ___  / /_\ \_ __   __ _| |_   _ _______ _ __ 
| | __| | __|  _  | | | | '_ \  |  __/ '__/ _ \|  _| | |/ _ \ |  _  | '_ \ / _` | | | | |_  / _ \ '__|
| |_\ \ | |_| | | | |_| | |_) | | |  | | | (_) | | | | |  __/ | | | | | | | (_| | | |_| |/ /  __/ |   
 \____/_|\__\_| |_/\__,_|_.__/  \_|  |_|  \___/|_| |_|_|\___| \_| |_/_| |_|\__,_|_|\__, /___\___|_|   
                                                                                    __/ |             
                                                                                   |___/              
```

---

## Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | **View Profile** | Displays full GitHub user info — name, location, followers, repos, and activity dates |
| 2 | **Repository Stats** | Detailed breakdown of every repo including stars, forks, issues, visibility, and links |
| 3 | **Commit History** | Lists all commits per repo (or the most recent 20 for larger repos) |
| 4 | **AI Profile Summary** | Sends profile + language + project data to Gemini and generates a structured career analysis report |
| 5 | **Save Report** | Optionally saves the AI-generated report as a `.txt` file under `AI Summaries/` |

---

## Project Structure

```
Github Profile Analyzer/
│
├── main.py               # Main application
├── prompt.txt            # System prompt for Gemini
├── example.env           # Template for environment variables
├── requirements.txt      # Python dependencies
└── AI Summaries/         # Auto-created folder for saved reports
    └── username.txt
```

---

## Requirements

- Python 3.9+
- A GitHub Personal Access Token
- A Google Gemini API Key

---

## Installation



**1. Install dependencies**

```bash
pip install -r requirements.txt
```

**2. Set up your environment variables**

Copy the example file and fill in your keys:

```bash
cp example.env .env
```

Then open `.env` and add your tokens (see [Getting API Keys](#getting-api-keys) below).

---

## Getting API Keys

### GitHub Personal Access Token

1. Go to → **https://github.com/settings/tokens**
2. Click **"Generate new token (classic)"**
3. Give it a name (e.g. `profile-analyzer`)
4. Select scopes: `read:user`, `repo` (public repos only needs `read:user`)
5. Click **Generate token** and copy it

### Google Gemini API Key

1. Go to → **https://aistudio.google.com/app/apikey**
2. Click **"Create API Key"**
3. Copy the generated key

---

## Environment Variables

Your `.env` file should look like this:

```env
GITHUB_TOKEN=your_github_personal_access_token_here
GEMINI_API=your_gemini_api_key_here
```

An `example.env` is included in the project as a reference template:

```env
# example.env — copy this to .env and fill in your values

# GitHub Personal Access Token
# Get yours at: https://github.com/settings/tokens
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Google Gemini API Key
# Get yours at: https://aistudio.google.com/app/apikey
GEMINI_API=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```


---

## Dependencies

Install all required libraries with:

```bash
pip install -r requirements.txt
```

`requirements.txt` contents:

```
requests
python-dotenv
halo
google-genai
```

---

## How to Run

```bash
python main.py
```

On launch you will be prompted to enter a GitHub username. The tool validates it against the GitHub API before proceeding. If the user is not found, it asks again.

```
Enter the GITHUB Username to Analyze :
> Any Github Username
```

Once a valid username is entered, the interactive menu appears:

```
--- Profile --------------------------------
[1]  View Profile         Display full GitHub user info
[2]  Repository Stats     Detailed breakdown of all repos
[3]  Commit History       Browse recent commits per repo
--- Analysis -------------------------------
[4]  AI Profile Summary   Full career analysis with score  [AI]
--------------------------------------------
[0]  Exit

Enter choice ›
```

Select a number and press Enter. After each action, press Enter to return to the menu.

---

## AI Report Structure

When you run option `[4] AI Profile Summary`, Gemini analyzes the developer's data and returns a structured terminal report covering:

```
DEVELOPER PROFILE   — Focus area, experience level, standout trait
LANGUAGES           — Aggregated usage %, ranked with labels
PROJECTS            — Per-repo complexity, score, strengths, gaps
HEALTH CHECK        — Bio, diversity, docs, community, consistency
STRENGTHS           — Evidence-backed positives
GAPS                — Honest list of what is missing
RECOMMENDATIONS     — 5 prioritized action items
CAREER DIRECTION    — Current role fit, 6-12 month target, key skill
SCORE /100          — Breakdown across 4 axes with verdict
```

You will be asked after the report whether to save it:

```
Do You want to save this response (Yes/No) ?
```

Saved reports are stored in the `AI Summaries/` folder as `username.txt`.

---

## Notes

- The tool analyzes the **top 5 repositories** (sorted by stars) for users with more than 5 repos
- For users with 5 or fewer repos, all repositories are analyzed
- Commit history is capped at the **most recent 20 commits** per repo for large repos
- The GitHub API has a rate limit of **5000 requests/hour** with an authenticated token



---

## License

MIT License — free to use, modify, and distribute.

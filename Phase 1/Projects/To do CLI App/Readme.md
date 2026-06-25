# 📋 TO DO APP — CLI Task Manager

```
████████╗ ██████╗     ██████╗  ██████╗      █████╗ ██████╗ ██████╗ 
╚══██╔══╝██╔═══██╗    ██╔══██╗██╔═══██╗    ██╔══██╗██╔══██╗██╔══██╗
   ██║   ██║   ██║    ██║  ██║██║   ██║    ███████║██████╔╝██████╔╝
   ██║   ██║   ██║    ██║  ██║██║   ██║    ██╔══██║██╔═══╝ ██╔═══╝ 
   ██║   ╚██████╔╝    ██████╔╝╚██████╔╝    ██║  ██║██║     ██║     
   ╚═╝    ╚═════╝     ╚═════╝  ╚═════╝     ╚═╝  ╚═╝╚═╝     ╚═╝     
```

> **Your daily tasks, simplified.**

A fully interactive, colorful command-line Task Manager built in Python. Tasks are persisted locally in a JSON file — no database, no dependencies, no internet required.

---

## 📑 Table of Contents

- [Features](#-features)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
  - [Interactive Menu Mode](#interactive-menu-mode)
  - [CLI Argument Mode](#cli-argument-mode)
- [Task Data Structure](#-task-data-structure)
- [Color Reference](#-color-reference)
- [Known Issues](#-known-issues)

---

## ✨ Features

- **Add Tasks** — Create tasks with an auto-incremented ID and automatic timestamp.
- **List Tasks** — View all tasks in a formatted display with a live progress bar.
- **Complete Tasks** — Mark any pending task as completed by ID.
- **Delete Tasks** — Remove a task permanently by ID.
- **Persistent Storage** — All tasks are saved to a local `data.json` file automatically.
- **Colorful Terminal UI** — ANSI color-coded output for a polished CLI experience.
- **Progress Bar** — Visual completion percentage shown when listing tasks.
- **Screen Clearing** — Each action clears the screen for a clean, focused UI.
- **Input Validation** — Handles invalid IDs and non-integer input gracefully.

---

## 📁 Project Structure

```
your-project/
│
├── main.py     # Main application file (Task, TaskManager, menu)
├── data.json           # Auto-created on first task addition (do not delete manually)
└── README.md           # This file
```

> `data.json` is created automatically when you add your first task. If it doesn't exist or is empty/corrupt, the app safely initializes with an empty list.

---

## ⚙️ Requirements

- **Python 3.6+**
- No third-party libraries required — only Python standard library modules are used:

| Module       | Purpose                                      |
|--------------|----------------------------------------------|
| `json`       | Reading and writing task data to `data.json` |
| `datetime`   | Generating timestamps when tasks are created |
| `pathlib`    | Building a cross-platform path to `data.json`|
| `os`         | Clearing the terminal screen (`cls`/`clear`) |

---


## 🖥️ Usage

### Interactive Menu Mode

Run the script directly to launch the interactive menu:

```bash
python main.py
```

You will see the following menu:

```
 [1] Add Task
 [2] List All Tasks
 [3] Complete Task
 [4] Delete Task
 [5] Exit
```

Enter the number corresponding to the action you want and follow the on-screen prompts.

#### Adding a Task

```
Enter your Choice > 1

============================================================
                        ➕ ADD TASK
============================================================

Enter the title : Buy groceries

 Task Added Successfully!
```

- The task is assigned the next available ID automatically.
- The current date and time is recorded as `created_at`.
- Status is set to `"pending"` by default.

#### Listing All Tasks

```
Enter your Choice > 2

============================================================
                       📋 ALL TASKS
============================================================
[=================---------] 60% Completed (3/5 Tasks)
------------------------------------------------------------
id           : 1
title        : Buy groceries
status       : completed
created_at   : 25/06/2026, 10:30:45
============================================================
...
```

- A progress bar shows the ratio of completed vs total tasks.
- `completed` statuses are displayed in **green**, `pending` in **yellow**.

#### Completing a Task

```
Enter your Choice > 3

============================================================
                      ✅ COMPLETE TASK
============================================================

Enter Task ID to mark it Complete : 2

 Task Marked Completed!
```

- If the entered ID doesn't exist, an error message is shown and you can try again.
- If a non-integer is entered, the input is rejected with a clear message.

#### Deleting a Task

```
Enter your Choice > 4

============================================================
                      ❌ DELETE TASK
============================================================

Enter Task ID to delete it : 3

 Task Deleted Successfully!
```

- Deletion is permanent. The task is removed from `data.json` immediately.
- If the ID is not found, an error message is shown.

---



## 🗂️ Task Data Structure

Each task is stored as a JSON object in `data.json` with the following fields:

```json
{
    "id": 1,
    "title": "Buy groceries",
    "status": "pending",
    "created_at": "25/06/2026, 10:30:45"
}
```

| Field        | Type    | Description                                          |
|--------------|---------|------------------------------------------------------|
| `id`         | integer | Unique identifier, auto-incremented from the max existing ID |
| `title`      | string  | The name/description of the task                     |
| `status`     | string  | Either `"pending"` or `"completed"`                  |
| `created_at` | string  | Timestamp in `DD/MM/YYYY, HH:MM:SS` format           |

A sample `data.json` with multiple tasks:

```json
[
    {
        "id": 1,
        "title": "Buy groceries",
        "status": "completed",
        "created_at": "25/06/2026, 10:30:45"
    },
    {
        "id": 2,
        "title": "Fix login bug",
        "status": "pending",
        "created_at": "25/06/2026, 11:15:00"
    }
]

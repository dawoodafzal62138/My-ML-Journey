

# 📁 Automated File Organizer 

A smart, fast, and interactive command-line tool built in Python to automatically sort and organize your cluttered folders. It categorizes files based on their extensions, provides a visual tree view of your directories, and keeps a detailed log of all file movements.

## ✨ Features

* **Smart Sorting:** Automatically categorizes files into specific folders (e.g., `Images`, `Documents`, `Videos`, `Scripts`, `Archives`) based on their file extensions.
* **GUI Folder Selection:** Uses an intuitive graphical dialog box (`tkinter`) to easily select target directories—no need to manually type out long file paths.
* **Tree Structure View:** Visualize your directory's layout directly in the terminal with a clean, tree-like structure.
* **Detailed Logging:** Keeps a persistent record of every moved file in a `logs.txt` file, tracking the original file name, destination category, date, and exact time of the move.
* **Zero External Dependencies:** Built entirely using Python's standard library. No `pip install` required!
* **Interactive Menu:** Easy-to-use, emoji-supported terminal interface for seamless navigation.

---

## 🛠️ Requirements

* **Python 3.6** or higher.
* (On Linux only) You may need to ensure `tkinter` is installed via your package manager if it didn't come bundled with your Python installation (e.g., `sudo apt-get install python3-tk`). Windows and macOS typically include it by default.

---

## 🚀 How to Use

1. Clone this repository or download the Python script to your local machine.
2. Open your terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script using Python:

```bash
python file_organizer.py

```

### 🗂️ Menu Options

Once the script is running, you will be presented with a menu:

1. **Organize Files:** Prompts you to select a folder, then automatically sorts all loose files inside it into categorized subfolders. Unrecognized formats are placed in an `others` folder.
2. **Show Files in Folder:** Prompts you to select a folder and displays a neat, visual breakdown of all its contents in the console.
3. **Show Logs:** Prints the complete history of your organized files directly to the terminal.
4. **Exit:** Closes the application.

---

## 📦 Supported File Categories

The script recognizes and sorts a massive variety of file extensions into the following default categories:

* **Images:** `.jpg`, `.png`, `.gif`, `.webp`, `.svg`, etc.
* **Documents:** `.pdf`, `.docx`, `.txt`, `.csv`, etc.
* **Spreadsheets:** `.xls`, `.xlsx`, `.ods`, etc.
* **Presentations:** `.ppt`, `.pptx`, `.key`, etc.
* **Videos:** `.mp4`, `.mkv`, `.avi`, `.mov`, etc.
* **Audio:** `.mp3`, `.wav`, `.flac`, etc.
* **Archives:** `.zip`, `.rar`, `.7z`, `.tar`, etc.
* **Programs:** `.exe`, `.msi`, `.apk`, etc.
* **Scripts:** `.py`, `.js`, `.cpp`, `.sh`, `.java`, etc.
* **Web:** `.html`, `.css`, `.jsx`, etc.
* **Data:** `.json`, `.xml`, `.sql`, `.yaml`, etc.
* **Fonts:** `.ttf`, `.otf`, `.woff`, etc.
* **Design:** `.psd`, `.ai`, `.fig`, etc.
* **Ebooks:** `.epub`, `.mobi`, `.azw3`
* **3D Models:** `.obj`, `.fbx`, `.stl`, etc.
* **Disk Images:** `.iso`, `.img`, `.dmg`
* **Logs & Backups:** `.log`, `.bak`
* **Shortcuts & Torrents:** `.lnk`, `.torrent`

---

## ⚠️ Notes

* The organizer does **not** move folders; it only sorts files located directly within the selected root directory.
* The log file (`logs.txt`) will be generated automatically in the same directory as the Python script.
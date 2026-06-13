import pathlib
import os
import shutil
from tkinter import filedialog
from datetime import datetime
import time
class file_organizer:
    def __init__(self , path , File_Categories):
        self.path = path
        self.file_categories = File_Categories
        dir = pathlib.Path(__file__).parent.resolve()
        self.LOG_PATH = dir / "logs.txt" 
        

    def organize(self):
        count = 0
        for file in os.listdir(self.path):
            path = os.path.join(self.path , file)
            
            if os.path.isfile(path):
                dir_to_make="others"
                ext = pathlib.Path(path).suffix.lower()
                for  key , values in self.file_categories.items():
                    if ext in values:
                            dir_to_make = key
            
                os.makedirs(os.path.join(self.path,dir_to_make) ,exist_ok = True)
                destination= os.path.join(self.path ,dir_to_make ,file)
                shutil.move(path , destination)
                count+=1
                with self.LOG_PATH.open("a", encoding="utf-8") as f:
                    f.write(f"📄 File      : {file}\n")
                    f.write(f"📂 Category  : {dir_to_make}\n")
                    f.write(f"📍 Moved To  : {os.path.join(self.path , dir_to_make)}\n")
                    f.write(f"📅 Date      : {datetime.now().strftime('%d-%m-%y')} \n")
                    f.write(f"🕜 Time      : {datetime.now().strftime('%H:%M:%S')}\n")
                    f.write("-" * 60 + "\n\n")

        print("📊 Files organized successfully!")
        print(f"Total files moved: {count}")
    def show_files(self ):
        print("\n" + "═" * 60)
        print("📂 FILE STRUCTURE VIEW")
        print("═" * 60)

        for item in os.listdir(self.path):

            full_path = os.path.join(self.path , item)

            if os.path.isdir(full_path):
                print(f"📁 {item} ")

                for file in os.listdir(full_path):
                    file_path= os.path.join(full_path , file)

                    if os.path.isfile(file_path):
                        print(f"    ├── 📄 {file}")
                    elif os.path.isdir(file_path):
                        print(f"    ├── 📁 {file}")
        
            elif os.path.isfile(full_path):
                print(f"📄 {item}")
        print("\n" + "═" * 60)




dir = pathlib.Path(__file__).parent.resolve()
LOG_PATH = dir / "logs.txt" 

def log():
    if LOG_PATH.exists():
        with LOG_PATH.open("r",encoding="utf-8") as f:
            data = f.read()
        

        if data.strip():
            
                print(data)
        else: 
            print("⚠️  Log File is Empty")

    else:
        print("\n⚠️  No logs Found")





FILE_CATEGORIES = {"Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp",".webp", ".svg", ".tiff", ".ico"],

                "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf",".odt", ".pages"],

                "Spreadsheets": [".xls", ".xlsx", ".csv", ".ods"],

                "Presentations": [".ppt", ".pptx", ".odp", ".key"],

                "Videos": [".mp4", ".avi", ".mkv", ".mov",".wmv", ".flv", ".webm", ".m4v"],

                "Audio": [".mp3", ".wav", ".aac", ".flac",".ogg", ".m4a", ".wma"],

                "Archives": [".zip", ".rar", ".7z", ".tar",".gz", ".bz2", ".xz"],

                "Programs": [".exe", ".msi", ".apk", ".app",".deb", ".rpm"],

                "Scripts": [".py", ".js", ".ts", ".java",".cpp", ".c", ".cs", ".php",".rb", ".go", ".rs", ".sh"],

                "Web": [".html", ".htm", ".css",".jsx", ".tsx"],

                "Data": [".json", ".xml", ".yaml",".yml", ".sql", ".db",".sqlite"],

                "Fonts": [".ttf", ".otf", ".woff",".woff2", ".eot"],

                "Design": [".psd", ".ai", ".xd",".fig", ".sketch"],

                "Ebooks": [".epub", ".mobi", ".azw3"],

                "3D Models": [".obj", ".fbx", ".stl",".blend", ".3ds"],

                "Disk Images": [".iso", ".img", ".dmg"],

                "Logs": [".log"],

                "Backups": [".bak", ".backup"],

                "Torrents": [".torrent"],

                "Shortcuts": [".lnk", ".url"]
}



def show_menu():
            print("\n" + "═" * 50)
            print("🗂️  FILE ORGANIZER MENU")
            print("═" * 50)
            print("1️⃣  Organize Files")
            print("2️⃣  Show Files in Folder")
            print("3️⃣  Show Logs")
            print("4️⃣  Exit")
            print("═" * 50)

if __name__ == "__main__":
    print("\n" + "╔" + "═" * 46 + "╗")
    print("║        📁 FILE ORGANIZER CLI SYSTEM          ║")
    print("║     Auto Sort • Clean • Fast • Smart         ║")
    print("╚" + "═" * 46 + "╝\n")
    time.sleep(1)
    while True:
        try:
            show_menu()
            choice= int(input("Enter Your Choice: "))
            if choice == 1: 
                path = filedialog.askdirectory(title="Select a Folder: ")
                if path:
                    f_o  = file_organizer(path , FILE_CATEGORIES)
                    f_o.organize()
                else:
                     print("⚠️ Please Enter The Path")
                     continue
            elif choice == 2:
                path = filedialog.askdirectory(title="Select a Folder: ")
                if path:
                    f_o  = file_organizer(path , FILE_CATEGORIES)
                    f_o.show_files()
                else:
                    print("⚠️ Please Enter The Path")
                    continue
                     
            elif choice ==3:
                log()
            elif choice ==4:
                exit()
            else:
                print("⚠️ Invalid Choice")
        except ValueError as e:
            print(f" ❌ Error : {e}")
        
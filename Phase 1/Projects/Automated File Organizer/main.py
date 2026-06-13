import pathlib
import os
import shutil
import sys
from tkinter import filedialog

class file_organizer:
    def __init__(self , path  ,File_Categories):
        self.path = path
        self.file_categories = File_Categories
        self.organize()

    def organize(self):
        
        for file in os.listdir(self.path):
            path = os.path.join(self.path , file)
            
            if os.path.isfile(path):
                dir_to_make="others"
                for  key , values in self.file_categories.items():
                    ext = pathlib.Path(path).suffix.lower()
                    if ext in values:
                            dir_to_make = key
            
                os.makedirs(os.path.join(self.path,dir_to_make) ,exist_ok = True)
                shutil.move(path , os.path.join(self.path,dir_to_make))
                print(f" {file} move to {os.path.join(self.path,dir_to_make)}")
                    














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

path = filedialog.askdirectory(title="Select a Folder: ")


if __name__ == "__main__":
    f_o  = file_organizer(path , FILE_CATEGORIES)
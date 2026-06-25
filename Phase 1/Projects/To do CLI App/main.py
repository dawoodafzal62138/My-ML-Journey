import json
import datetime
import pathlib
import os


BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
GREY ="\033[90m"
RESET = "\033[0m"
BRIGHT_RED = "\033[91m"


class Task:
    def __init__(self , id: int , title : str, status : str , created_at ):
        self.id = id
        self.title = title
        self.status = status
        self.created_at = created_at

    def to_dict(self):
        data = {
            "id" : self.id,
            "title" : self.title,
            "status" : self.status,
            "created_at" : self.created_at
        }
        return data


class TaskManager:
    def __init__(self , path : str):
        self.path = path

    
    def load_task(self):
        try:

            with self.path.open("r") as f: 
                data= json.load(f)
                return data
        except (json.JSONDecodeError , FileNotFoundError):
            return []            


    def get_next_id(self):
        data = self.load_task()
        if not data:
            return 1
        return max([item["id"] for item in data]) + 1

    
    
    def add_task(self  , title : str, status : str ):
        id = self.get_next_id()
        date_time = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        t= Task( id , title , status, date_time )
        self.data= t.to_dict()
        self.save_task()


    def save_task(self):
        data = self.load_task()
        data.append(self.data)
        with self.path.open("w" ) as f:
            json.dump(data, f ,indent=4)


    def delete_task(self  ,id : int):
        data = self.load_task()
        for item in data:
            if item["id"] == id:
                data.remove(item)
        with self.path.open("w" ) as f:
            json.dump(data, f ,indent=4)
        
    

    def compelete_task(self , id ):
        data = self.load_task()
        for item in data:
            if item["id"] == id:
                item["status"] = "completed"
        with self.path.open("w" ) as f:
            json.dump(data, f ,indent=4)

    
    
    def list_tasks(self):
        data = self.load_task()
        for item in data:
            print("="*60)
            for key , value in item.items():
                print(f"{key } : {value}")
            print("="*60)




def menu():
    os.system("cls" if os.name == "nt" else "clear")
    print(r"""
████████╗ ██████╗     ██████╗  ██████╗      █████╗ ██████╗ ██████╗ 
╚══██╔══╝██╔═══██╗    ██╔══██╗██╔═══██╗    ██╔══██╗██╔══██╗██╔══██╗
   ██║   ██║   ██║    ██║  ██║██║   ██║    ███████║██████╔╝██████╔╝
   ██║   ██║   ██║    ██║  ██║██║   ██║    ██╔══██║██╔═══╝ ██╔═══╝ 
   ██║   ╚██████╔╝    ██████╔╝╚██████╔╝    ██║  ██║██║     ██║     
   ╚═╝    ╚═════╝     ╚═════╝  ╚═════╝     ╚═╝  ╚═╝╚═╝     ╚═╝     
                                                                   
""")
    print(f"{CYAN}- {RESET}"*30)
    print(f"{MAGENTA}\t\tLearn -- Play -- Improve")
    print(f"{CYAN}- {RESET}"*30)
    print(f"{BLUE} [1] {GREY}Add Task")
    print(f"{BLUE} [2] {GREY}List ALl Task")
    print(f"{BLUE} [3] {GREY}Complete Task")
    print(f"{BLUE} [4] {GREY}Delete Task")
    print(f"{BLUE} [5] {GREY}Exit")
    choice= input(f"\t\n{GREEN}Enter your Choice > ")
    return choice








PATH  = pathlib.Path(__file__).parent.resolve() / "data.json"

    
if __name__ == "__main__":

    tm = TaskManager(PATH)
    actions={
        "1" : tm.add_task,
        "2" : tm.list_tasks,
        "3" : tm.compelete_task,
        "4" : tm.delete_task,
        "5" : exit
     }
    while True:
        choice = menu()
        if choice in actions:

            actions[choice]()
            input(f"{GREEN} Press Enter to Return to Menu ....")
        else:
            print(f"{BRIGHT_RED} Invalid Choice ")






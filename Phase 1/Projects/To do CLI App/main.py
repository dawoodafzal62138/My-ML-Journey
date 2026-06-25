import json
import datetime
import pathlib
import os


BLACK = "\033[30m"
RED = "\033[31m"
BRIGHT_GREEN = "\033[92m"
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

    
    
    def add_task(self   ):
        os.system("cls" if os.name == "nt" else "clear")
        print(f"\n{GREY}{'='*60}{RESET}")
        print(f"{MAGENTA}{'➕ ADD TASK'.center(60)}{RESET}")
        print(f"{GREY}{'='*60}{RESET}")
        title =  input(f"\n{BLUE}Enter the title : {RESET}")
        id = self.get_next_id()
        date_time = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        t= Task( id , title , "pending", date_time )
        self.data= t.to_dict()
        self.save_task()
        print(f"{BRIGHT_GREEN}\n Task Added Succesfully!")








    def save_task(self):
        data = self.load_task()
        data.append(self.data)
        with self.path.open("w" ) as f:
            json.dump(data, f ,indent=4)


    def delete_task(self ):
        os.system("cls" if os.name == "nt" else "clear")
        print(f"\n{GREY}{'='*60}{RESET}")
        print(f"{MAGENTA}{'❌ DELETE TASK'.center(60)}{RESET}")
        print(f"{GREY}{'='*60}{RESET}")
        data = self.load_task()
        while True:
            try:
                found  = False
                id  = int(input(f"\n{BLUE}Enter Task ID to delete it : {RESET}" ))
                for item in data:
                    if item["id"] == id:
                        found = True
                        break
                    
                if not found:
                    print(f"{BRIGHT_RED} \nTask with id {id} is not Found ! {RESET}")
                    continue
                else:
                    break 
            except ValueError :
                print(f"{BRIGHT_RED} \nInvalid Choice")

        
        for item in data:
            if item["id"] == id:
                data.remove(item)
        with self.path.open("w" ) as f:
            json.dump(data, f ,indent=4)
        print(f"{BRIGHT_GREEN}\n Task Deleted Succesfully!")

        
        
        
    

    def compelete_task(self):

        os.system("cls" if os.name == "nt" else "clear")
        print(f"\n{GREY}{'='*60}{RESET}")
        print(f"{MAGENTA}{'✅ COMPLETE TASK'.center(60)}{RESET}")
        print(f"{GREY}{'='*60}{RESET}")

        data = self.load_task()
        while True:
            try:
                found  = False
                id  = int(input(f"\n{BLUE}Enter Task ID to mark  it Ccomplete : {RESET}" ))
                for item in data:
                    if item["id"] == id:
                        found = True
                        break
                    
                if not found:
                    print(f"{BRIGHT_RED} \nTask with id {id} is not Found ! {RESET}")
                    continue
                else:
                    break    
            except ValueError :
                print(f"{BRIGHT_RED} \nInvalid Choice")


        for item in data:
            if item["id"] == id:
                item["status"] = "completed"
        with self.path.open("w" ) as f:
            json.dump(data, f ,indent=4)
        print(f"{BRIGHT_GREEN} \nTask Marked Completed !")

    
    
    def list_tasks(self):
        data = self.load_task()
        os.system("cls" if os.name == "nt" else "clear")
        
        print(f"\n{GREY}{'='*60}{RESET}")
        print(f"{MAGENTA}{'📋 ALL TASKS'.center(60)}{RESET}")
        print(f"{GREY}{'='*60}{RESET}")
       
        if not data:
            print(f"{YELLOW}\nNo tasks found in your list!{RESET}")
            return
      
        total = len(data)
        
        if total > 0:
            completed = 0
            for item in data:
                if item["status"] == "completed":
                    completed += 1
            
            percent = (completed / total) * 100
            
            BAR_WIDTH = 30
            filled_chars = int(BAR_WIDTH * (completed / total))
            empty_chars = BAR_WIDTH - filled_chars
            
            bar_string = f"{BRIGHT_GREEN}{'=' * filled_chars}{RESET}{GREY}{'-' * empty_chars}{RESET}"
            
            print(f"[{bar_string}] {BRIGHT_GREEN}{percent:.0f}% Completed ({completed}/{total} Tasks){RESET}")
            print(f"{GREY}{'-'*60}{RESET}")
        
        
        print(f"{GREY}{'='*60}{RESET}")
        for item in data:
            for key, value in item.items():
                key_formatted = f"{CYAN}{key:<12}{RESET}"
                
                if key == "status":
                    if value == "completed":
                        value_formatted = f"{BRIGHT_GREEN}{value}{RESET}"
                    else:
                        value_formatted = f"{YELLOW}{value}{RESET}"
                
                else:
                    value_formatted = f"{WHITE}{value}{RESET}"
                
                print(f"{key_formatted} : {value_formatted}")
                
            print(f"{GREY}{'='*60}{RESET}")




def menu():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{BRIGHT_GREEN}")
    print(r"""
████████╗ ██████╗     ██████╗  ██████╗      █████╗ ██████╗ ██████╗ 
╚══██╔══╝██╔═══██╗    ██╔══██╗██╔═══██╗    ██╔══██╗██╔══██╗██╔══██╗
   ██║   ██║   ██║    ██║  ██║██║   ██║    ███████║██████╔╝██████╔╝
   ██║   ██║   ██║    ██║  ██║██║   ██║    ██╔══██║██╔═══╝ ██╔═══╝ 
   ██║   ╚██████╔╝    ██████╔╝╚██████╔╝    ██║  ██║██║     ██║     
   ╚═╝    ╚═════╝     ╚═════╝  ╚═════╝     ╚═╝  ╚═╝╚═╝     ╚═╝     
                                                                   
""")
    print(f"{CYAN}- {RESET}"*30)
    print(f"{MAGENTA}\t\tYour daily tasks, simplified")
    print(f"{CYAN}- {RESET}"*30)
    print(f"{BLUE} [1] {GREY}Add Task")
    print(f"{BLUE} [2] {GREY}List ALl Task")
    print(f"{BLUE} [3] {GREY}Complete Task")
    print(f"{BLUE} [4] {GREY}Delete Task")
    print(f"{BLUE} [5] {GREY}Exit")
    choice= input(f"\t\n{BRIGHT_GREEN}Enter your Choice > ")
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
            input(f"{BRIGHT_GREEN} \nPress Enter to Return to Menu ....")
        else:
            print(f"{BRIGHT_RED} \nInvalid Choice ")






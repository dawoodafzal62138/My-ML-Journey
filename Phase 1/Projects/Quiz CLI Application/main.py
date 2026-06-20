import json
import pathlib
from halo import Halo
import os
from google import genai
from google.genai import errors
from dotenv import load_dotenv
import sys
import datetime


# Load the api key from gemini
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Path to Store history
PATH = pathlib.Path(__file__).parent.resolve() / "history.txt"


# Path of System_instruction to Gemini
PROMPT_PATH = pathlib.Path(__file__).parent.resolve() / "prompt.txt"
with PROMPT_PATH.open("r") as f:
    prompt = f.read()


# AscII colour Codes
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
BRIGHT_RED = "\033[91m"
GREY = "\033[90m"
BOLD = "\033[1m"
BRIGHT_WHITE = "\033[97m"
BRIGHT_YELLOW = "\033[93m"



class quiz_app:
    def __init__(self, prompt , path ):
        self.system_prompt = prompt
        self.path = path

    

    # Get Response from gemini
    def get_response(self , text):
        # start the spinner
        spinner = Halo("Generating Quiz ", "cyan", "blue" ,spinner="dots3")
        try:
            spinner.start()
            # made client and give the system instruction
            client = genai.Client(api_key=GEMINI_API_KEY)
            session =client.chats.create(
                model="gemini-3.1-flash-lite", config={
                    "system_instruction":self.system_prompt,
                    "temperature" : 0.7
                },)
            # get response
            response = session.send_message(text)
            spinner.stop()
            
            return (json.loads(response.text))
        
        except errors.ClientError as e: 
            if spinner: 
                spinner.stop()
            print(f"\t{BRIGHT_RED} {e}")

    
    # Mani Function :  Starts the Quiz
    def start_quiz(self ):
        subject , difficulty =  self.get_difficulty_subject()
        
        text =f" subject : {subject}  ,  difficulty : {difficulty}"
        

        quiz_response = self.get_response(text)
        point = 0
        if not isinstance(quiz_response ,list) or len(quiz_response)!= 10:
            for i , question in enumerate(quiz_response , start= 1):
                os.system("cls" if os.name == "nt" else "clear")
                print(f"\n {GREEN}{BOLD}Question {i} : {BRIGHT_WHITE} {question['question']}\n")
                for j , option in enumerate(question["options"] ,start = 1):
                    print(f"{BLUE} {j}. {GREY}{option}{RESET}")
                while True:
                    try:
                        choice= int(input(f"\n{GREEN}Enter your Answer >  "))
                        if question["options"][choice-1] == question["answer"]:
                            point +=1
                        break
                    except ValueError:
                        print(f"{BRIGHT_RED} Invalid Choice ")
                        continue
            print(f"\n{GREEN}Correct : {point}\t{RED}Incorrect : {10 - point}\n")
            with self.path.open("a" ,encoding="utf-8" ) as f:
                f.write("\n"+f"{BLUE}= {RESET}" * 30)
                Date= datetime.datetime.now().strftime("%d-%m-%Y")
                Time = datetime.datetime.now().strftime("%H:%M:%S")
                f.write(f"\n{CYAN}Date       : {Date:<20}   Time       : {Time}{RESET}")
                f.write(f"\n{MAGENTA}Category   : {subject:<20}   Difficulty : {difficulty}{RESET}")
                f.write(f"\n{GREEN}Correct    : {point:<20}   {RED}Incorrect  : {10 - point}\n{RESET}")
                f.write(f"{BLUE}= {RESET}" * 30+"\n\n")
        else:
            print(f"{BRIGHT_RED} Invalid Respose By AI , Try Again")

    # Get difficulty Level and the Subject from the User
    def get_difficulty_subject(self):
        subjects = [
        "General Knowledge",
        "Science",
        "Mathematics",
        "History",
        "Geography",
        "Technology",
        "Sports",
        "Entertainment",
        "Literature",
        "Business",
        "Health",
        "Nature",
        "Politics",
        "Art & Culture",
        "Mixed Quiz"
    ]
        
        difficulty = ["hard" , "medium" ,"easy"]
        while True:
            try:
                os.system("cls" if os.name == "nt" else "clear")
                print(f"{BLUE}{BOLD}Select Subject > \n{RESET}")
                for index , item in enumerate(subjects, start=1):
                    print(f"{BLUE} [{index}]  {GREY}{item}")
                choice= int(input(f"\t\n{GREEN}Enter your Choice > "))
                if choice > 0 and choice <= len(subjects):
                    selected_subject = subjects[choice-1]
                    break
                else:
                    print(f"\n{BRIGHT_RED} Invalid Choice ")
            except:
                print(f"\n {BRIGHT_RED} Invalid Choice")
        while True:
            try:
                os.system("cls" if os.name == "nt" else "clear")
                print(f"{BLUE}{BOLD}Select Difficulty > \n")
                for index , item in enumerate(difficulty, start=1):
                    print(f"{BLUE} [{index}]  {GREY}{item}")
                choice= int(input(f"\t\n{GREEN}Enter your Choice > "))
                if choice > 0 and choice <= len(difficulty):
                    selected_difficulty = difficulty[choice-1]
                    break
                else:
                    print(f"\n{BRIGHT_RED} Invalid Choice ")
            except ValueError:
                print(f"\n{BRIGHT_RED} Invalid Choice")

        return selected_subject ,selected_difficulty 




    # Read the history from the file and print in the terminal
    def get_history(self):
        if os.path.isfile(self.path):
            with self.path.open("r") as f:
                data = f.read()
            os.system("cls" if os.name=="nt" else "clear")
            print(f"{BOLD}{BRIGHT_YELLOW}   📜 QUIZ HISTORY 📜   {RESET}\n")
            print(data)
        else:
            print(f"{RED} NO History of Quiz Found ! {RESET}" )

            












def menu():
    os.system("cls" if os.name == "nt" else "clear")
    print(r"""
 ██████╗ ██╗   ██╗██╗███████╗     █████╗ ██████╗ ██████╗ 
██╔═══██╗██║   ██║██║╚══███╔╝    ██╔══██╗██╔══██╗██╔══██╗
██║   ██║██║   ██║██║  ███╔╝     ███████║██████╔╝██████╔╝
██║▄▄ ██║██║   ██║██║ ███╔╝      ██╔══██║██╔═══╝ ██╔═══╝ 
╚██████╔╝╚██████╔╝██║███████╗    ██║  ██║██║     ██║     
 ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝     ╚═╝     
""")
    print(f"{CYAN}- {RESET}"*30)
    print(f"{MAGENTA}\t\tLearn -- Play -- Improve")
    print(f"{CYAN}- {RESET}"*30)
    print(f"{BLUE} [1] {GREY}Start Quiz")
    print(f"{BLUE} [2] {GREY}See History")
    print(f"{BLUE} [3] {GREY}Exit")
    choice= input(f"\t\n{GREEN}Enter your Choice > ")
    return choice









    
if __name__ == "__main__":

    quiz = quiz_app(prompt , PATH)
    actions={
        "1" : quiz.start_quiz,
        "2" : quiz.get_history,
        "3" : sys.exit
    }
    while True:
        choice = menu()
        if choice in actions:

            actions[choice]()
            input(f"{GREEN} Press Enter to Return to Menu ....")
        else:
            print(f"{BRIGHT_RED} Invalid Choice ")


import json
from halo import Halo
import os
from google import genai
from dotenv import load_dotenv
import sys


# Load the api key from gemini
load_dotenv()
GENAI_API_KEY = os.getenv("GENAI_API_KEY")






class quiz_app:
    def __init__(self, prompt):
        self.system_prompt = prompt

    
    def get_response(self , text):
        # start the spinner
        spinner = Halo("Generating Quiz ", "cyan", "blue" ,spinner="dots3")
        spinner.start()
        # made client and give the system instruction
        client = genai.Client(api_key=GENAI_API_KEY)
        session =client.chat.create(
            model="gemini-3.0-flash-lite", config={
                "system_prompt":self.system_prompt,
            },)
        # get response
        response = session.send_message(text)
        spinner.stop()
        return response
    

    def start_quiz(self , subject, difficulty):
        text ={
            "subject" : subject,
            "difficulty" : difficulty,
        }




        quiz_response = self.get_response(text)
        point = 0
        if quiz_response:
            for i , question in enumerate(quiz_response , start= 1):
                os.system("cls" if os.name == "nt" else "clear")
                print(f"\033[1mQuestion {i}:\033[0m {question['question']}")
                for j , option in enumerate(question["options"] ,start = 1):
                    print(f"\033[34m {j}. {option}")
                while True:
                    try:
                        choice= int(input("\t\033[32mEnter your Answer >"))
                        if choice == quiz_response["answer"]:
                            point +=1
                            print(f"\t\033[32mCorrect : {point}\t\033[31mIncorrect : {10 - point}")
                    except ValueError:
                        continue











def get_difficulty_subject():
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
            print("\033[34;1mSelect Subject > \n")
            for index , item in enumerate(subjects, start=1):
                print(f"\033[32m [{index}]  \033[37m{item}")
            choice= int(input("\t\n\033[32mEnter your Choice > "))
            if choice > 0 and choice <= len(subjects):
                selected_subject = subjects[choice-1]
                break
            else:
                print("\n\033[31m Invalid Choice ")
        except:
            print("\n \033[31 Invalid Choice")
    while True:
        try:
            os.system("cls" if os.name == "nt" else "clear")
            print("\033[34;1mSelect Difficulty > \n")
            for index , item in enumerate(difficulty, start=1):
                print(f"\033[32m [{index}]  \033[37m{item}")
            choice= int(input("\t\n\033[32mEnter your Choice > "))
            if choice > 0 and choice <= len(subjects):
                selected_difficulty = difficulty[choice-1]
                break
            else:
                print("\n\033[31m Invalid Choice ")
        except:
            print("\n\033[31 Invalid Choice")

    return selected_difficulty ,selected_subject



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
    print("- "*30)
    print("\033[36m\t\tLearn -- Play -- Improve")
    print("- "*30)
    print("\033[34m [1] \033[90mStart Quiz")
    print("\033[34m [2] \033[90mSee History")
    print("\033[34m [3] \033[90mExit")
    choice= input("\t\n\033[32mEnter your Choice > ")
    return choice







    
if __name__ == "__main__":

    # difficulty , subject = get_difficulty_subject()
    # print(difficulty, subject)
    # menu()
    quiz = quiz_app()
    actions={
        "1" : quiz.start_quiz,
        "2" : quiz.see_history,
        "3" : sys.exit
    }
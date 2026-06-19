import json
import requests
from halo import Halo
import os
from google import genai
from dotenv import load_dotenv


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











def get_difficulty():
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

    
if __name__ == "__main__":



    quiz = quiz_app()
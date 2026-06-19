import json
import requests
from halo import Halo
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

GENAI_API_KEY = os.getenv("GENAI_API_KEY")






class quiz_app:
    def __init__(self, prompt):
        self.system_prompt = prompt

    
    def get_response(self , text):
        spinner = Halo("Generating Quiz ", "cyan", "blue" ,spinner="dots3")
        spinner.start()
        client = genai.Client(api_key=GENAI_API_KEY)
        session =client.chat.create(
            model="gemini-2.0-flash", config={
                "system_prompt":self.system_prompt,
            },)
        response = session.send_message(text)
        spinner.stop()
        return response
    

    


















    
if __name__ == "__main__":
    quiz = quiz_app()
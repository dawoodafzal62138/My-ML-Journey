import os
import pathlib
import json
import requests
from dotenv import load_dotenv


load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = { 
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "X-GitHub-Api-Version": "2026-03-10"
   }
PATH = pathlib.Path(__file__).parent.resolve() / "reports.json"




class profile_analyzer:
    def __init__(self, username , Path , Url ):
        self.path = Path
        self.url=Url
        self.username= username



    def get_user_profile(self):
        pass


    def calculate_repository_stats(self):
        pass


    def get_repository_languages(self, repo_name):
        pass

    def language_stats(self):
        pass

    def analyze_commits(self):
        pass


def get_username():
    pass


url="https://api.github.com/users/dawoodafzal62138/repos"
url="https://api.github.com/"



r= requests.get(url,headers=HEADERS).json()


with PATH.open("w") as f:
    json.dump(r , f, indent=4 )




# if __name__ == "__main__":
#     pass
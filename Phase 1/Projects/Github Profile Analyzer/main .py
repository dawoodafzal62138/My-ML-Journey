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
    def __init__(self, username , Path , Url  , HEADERS):
        self.path = Path
        self.url=Url
        self.username= username
        self.HEADERS=HEADERS

        

    
    def get_response(self , url ):
        response = requests.get(url ,headers=self.HEADERS).json()
        return response

    def get_user_profile(self):
        profile_url = self.url + f"users/{self.username}"
        response = self.get_response(profile_url)
        print("\n" + "=" * 50)
        print("GITHUB USER PROFILE")
        print("=" * 50)

        print(f"Name                : {response['name']}")
        print(f"User ID             : {response['id']}")
        print(f"Location            : {response['location']}")
        print(f"Company             : {response['company']}")
        print(f"Email               : {response['email']}")
        print(f"Twitter Username    : {response['twitter_username']}")

        print("\n--- Account Information ---")
        print(f"Profile URL         : {response['html_url']}")
        print(f"Followers           : {response['followers']}")
        print(f"Public Repositories : {response['public_repos']}")

        print("\n--- Activity Information ---")
        print(f"Account Created On  : {response['created_at'].split('T')[0]}")
        print(f"Last Updated On     : {response['updated_at'].split('T')[0]}")

        print("=" * 50) 



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


# url="https://api.github.com/users/dawoodafzal62138/repos"
url="https://api.github.com/"



r= requests.get(url,headers=HEADERS).json()


# with PATH.open("w") as f:
#     json.dump(r , f, indent=4 )




if __name__ == "__main__":
    pa= profile_analyzer("dawoodafzal62138", PATH , url , HEADERS)
    pa.get_user_profile()


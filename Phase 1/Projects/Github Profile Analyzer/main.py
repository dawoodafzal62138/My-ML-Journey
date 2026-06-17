import os
import pathlib
import requests
from dotenv import load_dotenv
from halo import Halo
from google import genai
from google.genai import errors
import sys
import time

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GEMINI_API  = os.getenv("GEMINI_API")
base_url="https://api.github.com/"


prompt_path = pathlib.Path(__file__).parent.resolve() / "prompt.txt"

with prompt_path.open("r") as f :
    prompt = f.read()


HEADERS = { 
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "X-GitHub-Api-Version": "2026-03-10"
   }

    

def typewriter(text , delay = 0.001):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)    
    print()

class profile_analyzer:
    def __init__(self, username , Url  , HEADERS , system_prompt):
        
        self.url=Url
        self.username= username
        self.HEADERS=HEADERS
        self.system_prompt= system_prompt

        

    
    def get_response(self , url ):
        try:
            response = requests.get(url ,headers=self.HEADERS).json()
            return response
        except Exception as e:
            print("API ERROR: ", e)
            return []
    def get_user_profile(self):
        profile_url = self.url + f"users/{self.username}"
        response = self.get_response(profile_url)
        if response:
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
        else:
            print("An Unexpected error occurred ! ")


    def calculate_repository_stats(self):
        repos_url = self.url + f"users/{self.username}/repos"
        response = self.get_response(repos_url)
        if response:
            for index ,repo in enumerate(response , start= 1):
                print("\n" + "=" * 60)
                print(f"GITHUB REPOSITORY {index} REPORT")
                print("=" * 60)

                # Repository Information
                print("\n[ Repository Information ]")
                print(f"Repository Name     : {repo['name']}")
                print(f"Full Name           : {repo['full_name']}")
                print(f"Description         : {repo['description'] or 'Not Provided'}")
                print(f"Owner               : {repo['owner']['login']}")
                print(f"Visibility          : {repo['visibility'].title()}")
                print(f"Primary Language    : {repo['language']}")
                print(f"Default Branch      : {repo['default_branch']}")
                print(f"Repository Size     : {repo['size']} KB")

                # URLs
                print("\n[ Repository Links ]")
                print(f"GitHub URL          : {repo['html_url']}")
                print(f"Clone URL           : {repo['clone_url']}")
                print(f"SSH URL             : {repo['ssh_url']}")

                # Activity Information
                print("\n[ Activity ]")
                print(f"Created On          : {repo['created_at'].split('T')[0]}")
                print(f"Last Updated        : {repo['updated_at'].split('T')[0]}")
                print(f"Last Push           : {repo['pushed_at'].split('T')[0]}")

                # Statistics
                print("\n[ Statistics ]")
                print(f"Stars               : {repo['stargazers_count']}")
                print(f"Watchers            : {repo['watchers_count']}")
                print(f"Forks               : {repo['forks_count']}")
                print(f"Open Issues         : {repo['open_issues_count']}")

                # Features
                print("\n[ Features ]")
                print(f"Issues Enabled      : {repo['has_issues']}")
                print(f"Projects Enabled    : {repo['has_projects']}")
                print(f"Wiki Enabled        : {repo['has_wiki']}")
                print(f"Pages Enabled       : {repo['has_pages']}")
                print(f"Discussions Enabled : {repo['has_discussions']}")

                # Repository Status
                print("\n[ Status ]")
                print(f"Archived            : {repo['archived']}")
                print(f"Disabled            : {repo['disabled']}")
                print(f"Template Repository : {repo['is_template']}")
                print(f"Forked Repository   : {repo['fork']}")

                print("=" * 60 +"\n\n")
        else:
            print("An Unexpected error occurred ! ")

    def analyze_commits(self):
        repos_url = self.url + f"users/{self.username}/repos"
        response = self.get_response(repos_url)
        if response:

            for index  ,  repo in enumerate(response ,start=1):
                repo_name = repo["name"]
                repo_url = repo["commits_url"].split("{")[0]    
                repo_commits =  self.get_response(repo_url)
                print("\n" + "=" * 60)
                print(f"{index}.  📦{repo_name}")
                print("=" * 60)

                print(f"\nTotal Commits : {len(repo_commits)}")
                if len(repo_commits) < 20:
                    print("\nAll Commits")
                    print("-" * 15)
                    for commit in repo_commits:
                        sha =commit["sha"]
                        message= commit["commit"]["message"]
                        date= commit["commit"]["author"]["date"]
                        print(f"[{sha}] {date}  {message}")
                    print("=" * 60+"\n\n")
                else:
                    print("\nRecent 20 Commits")
                    print("-" * 15)
                    for commit in repo_commits[:20]:
                        sha =commit["sha"]
                        message= commit["commit"]["message"]
                        date= commit["commit"]["author"]["date"]
                        print(f"[{sha}] {date}  {message}")
                    print("=" * 60+"\n\n")

        else:
            print("An Unexpected error occurred ! ")




    def AI_summary(self):
        spinner = Halo("Fetching Data", color="cyan" , spinner="dots2") 
        spinner.start()
        url= self.url + f"users/{self.username}"
        response = self.get_response(url)
        url = self.url + f"users/{self.username}/repos"
        repo_response = self.get_response(url)
        profile_summary={}
        if response:
            profile_summary = {
            "Name" :response["name"],
            "bio" : response["bio"],
            "followers": response["followers"],
            "following" : response["following"],
            "public_repos": response["public_repos"],
            "account_created_at" : response["created_at"] ,
            "last_updated_at" : response["updated_at"],
            }
        
        if repo_response:
            repos_sorted = sorted(
            repo_response,
            key=lambda r: r["stargazers_count"],
            reverse=True
            )


            top_projects = []
            languages_summary =[]
            if len(repo_response) > 5:
                for repo  in repos_sorted[:5]:
                    url = repo["commits_url"].split("{")[0]
                    commit_len = len(self.get_response(url))
                    project = {"name" : repo["name"], "description" : repo["description"], "language" : repo["language"] , "commits" : commit_len , "size": repo["size"] , "Stars" : repo["stargazers_count"], "created_at":repo["created_at"].split("T")[0] , "updated_at":repo["updated_at"].split("T")[0] , "pushed_at" : repo["pushed_at"].split("T")[0]}
                    top_projects.append(project)
                    url = repo["languages_url"]
                    language_response = self.get_response(url)
                    for key , value in language_response.items():
                       languages_summary.append({key: value})
            else:
                for repo  in repo_response:
                    url = repo["commits_url"].split("{")[0]
                    commit_len = len(self.get_response(url))
                    project = {"name" : repo["name"], "description" : repo["description"], "language" : repo["language"] , "commits" : commit_len , "size": repo["size"] , "Stars" : repo["stargazers_count"], "created_at":repo["created_at"].split("T")[0] , "updated_at":repo["updated_at"].split("T")[0] , "pushed_at" : repo["pushed_at"].split("T")[0]}
                    top_projects.append(project)
                    url = repo["languages_url"]
                    language_response = self.get_response(url)
                    for key , value in language_response.items():
                        languages_summary.append({key : value})
        spinner.stop()
        print("All Information Fetched ! ")
        
      
        if profile_summary  and languages_summary and top_projects: 
            spinner = Halo("Thinking" , "cyan" , spinner="dots8")
            spinner.start()
            data = {"profile_summary" : profile_summary , "languages_summary" : languages_summary, "top_projects": top_projects}
            text = self.AI_response(data)
            spinner.stop()
            typewriter(text)
            while True:
                choice  = input("Do You want to save this response (Yes/No) ?")
                if choice.lower().strip() == "yes":
                    summary_folder = pathlib.Path(__file__).parent.resolve() / "AI Summaries"
                    os.makedirs(summary_folder , exist_ok=True)
                    with open(f"{summary_folder}/{self.username}.txt" , "w") as f:
                        f.write(text)
                        typewriter("Summary Saved Successfully ! ", delay=0.01)
                        break
                elif choice.lower().strip() == "no":
                    break
                else:
                    typewriter("Invalid Choice !" ,delay=0.01)


    def AI_response(self ,data):
        try:
            client = genai.Client(api_key=GEMINI_API)
            session = client.chats.create(model ="gemini-3.1-flash-lite" , config={"system_instruction": self.system_prompt})
            response = session.send_message(str(data))
            return response.text
        except errors.ClientError as e:
            return f"Error: {e}"




def get_username():
    while True:
        typewriter("Enter the GITHUB Username to Analyze : " ,delay=0.01)
        username  = input()
        response = requests.get(f"{base_url}users/{username.strip()}" ,headers= HEADERS).json()
        if "id" in response:
            return username.strip()
        else:
            print("\033[31m  User not found.\033[0m")






def show_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print("\033[34m")  # blue
    print(r""" 
     ██████╗ ██╗████████╗██╗  ██╗██╗   ██╗██████╗     ██████╗ ██████╗  ██████╗ ███████╗██╗██╗     ███████╗    
    ██╔════╝ ██║╚══██╔══╝██║  ██║██║   ██║██╔══██╗    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝██║██║     ██╔════╝    
    ██║  ███╗██║   ██║   ███████║██║   ██║██████╔╝    ██████╔╝██████╔╝██║   ██║█████╗  ██║██║     █████╗      
    ██║   ██║██║   ██║   ██╔══██║██║   ██║██╔══██╗    ██╔═══╝ ██╔══██╗██║   ██║██╔══╝  ██║██║     ██╔══╝      
    ╚██████╔╝██║   ██║   ██║  ██║╚██████╔╝██████╔╝    ██║     ██║  ██║╚██████╔╝██║     ██║███████╗███████╗    
     ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝     ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚══════╝    
                                                                                                          """)
    print(r"""
                 █████╗ ███╗   ██╗ █████╗ ██╗  ██╗   ██╗███████╗███████╗██████╗ 
                ██╔══██╗████╗  ██║██╔══██╗██║  ╚██╗ ██╔╝╚══███╔╝██╔════╝██╔══██╗
                ███████║██╔██╗ ██║███████║██║   ╚████╔╝   ███╔╝ █████╗  ██████╔╝
                ██╔══██║██║╚██╗██║██╔══██║██║    ╚██╔╝   ███╔╝  ██╔══╝  ██╔══██╗
                ██║  ██║██║ ╚████║██║  ██║███████╗██║   ███████╗███████╗██║  ██║
                ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝""")
    print("\033[0m")  # reset
    print("  v1.0.0  |  GitHub API v2026  |  Gemini 3.1 Flash Lite\n")
    print("  \033[90m--- Profile --------------------------------\033[0m")
    print("  \033[97m[1]\033[0m  View Profile         Display full GitHub user info")
    print("  \033[97m[2]\033[0m  Repository Stats     Detailed breakdown of all repos")
    print("  \033[97m[3]\033[0m  Commit History       Browse recent commits per repo")
    print("  \033[90m--- Analysis -------------------------------\033[0m")
    print("  \033[97m[4]\033[0m  AI Profile Summary   Full career analysis with score  \033[34m[AI]\033[0m")
    print("  \033[90m--------------------------------------------\033[0m")
    print("  \033[31m[0]\033[0m  Exit\n")
    return input("  Enter choice › ").strip()


if __name__ == "__main__":
    username = get_username()




    pa = profile_analyzer(username, base_url, HEADERS, prompt)
    actions = {
        "1": pa.get_user_profile,
        "2": pa.calculate_repository_stats,
        "3": pa.analyze_commits,
        "4": pa.AI_summary,
    }
    while True:
        choice = show_menu()
        if choice == "0":
            print("  Goodbye.")
            break
        elif choice in actions:
            actions[choice]()
            input("\n  Press Enter to return to menu...")
        else:
            print("  Invalid choice.")



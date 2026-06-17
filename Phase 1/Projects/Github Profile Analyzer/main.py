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
        sys.stdout.write(f"\033[94m{char}")
        sys.stdout.flush()
        time.sleep(delay)    
    print("\033[0m")

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
            print("\n\033[34m" + "=" * 50 + "\033[0m")
            print("\033[96m  GITHUB USER PROFILE\033[0m")
            print("\033[34m" + "=" * 50 + "\033[0m")

            print(f"\033[90mName                :\033[0m \033[97m{response.get('name', 'Not Provided')}\033[0m")
            print(f"\033[90mUser ID             :\033[0m \033[97m{response.get('id')}\033[0m")
            print(f"\033[90mLocation            :\033[0m \033[97m{response.get('location', 'Not Provided')}\033[0m")
            print(f"\033[90mCompany             :\033[0m \033[97m{response.get('company', 'Not Provided')}\033[0m")
            print(f"\033[90mEmail               :\033[0m \033[97m{response.get('email', 'Not Provided')}\033[0m")
            print(f"\033[90mTwitter Username    :\033[0m \033[97m{response.get('twitter_username', 'Not Provided')}\033[0m")

            print("\n\033[96m--- Account Information ---\033[0m")
            print(f"\033[90mProfile URL         :\033[0m \033[94m{response.get('html_url')}\033[0m") # Blue for URL
            print(f"\033[90mFollowers           :\033[0m \033[97m{response.get('followers')}\033[0m")
            print(f"\033[90mPublic Repositories :\033[0m \033[97m{response.get('public_repos')}\033[0m")

            print("\n\033[96m--- Activity Information ---\033[0m")
            print(f"\033[90mAccount Created On  :\033[0m \033[97m{response['created_at'].split('T')[0]}\033[0m")
            print(f"\033[90mLast Updated On     :\033[0m \033[97m{response['updated_at'].split('T')[0]}\033[0m")

            print("\033[34m" + "=" * 50 + "\033[0m\n") 
        else:
            print("\033[31m  [!] An Unexpected error occurred!\033[0m")


    def calculate_repository_stats(self):
        repos_url = self.url + f"users/{self.username}/repos"
        response = self.get_response(repos_url)
        if response:
            for index ,repo in enumerate(response , start= 1):
                print("\033[34m" + "=" * 60 + "\033[0m")
                print(f"\033[96m  GITHUB REPOSITORY {index} REPORT\033[0m")
                print("\033[34m" + "=" * 60 + "\033[0m")

                # Repository Information
                print("\n\033[96m[ Repository Information ]\033[0m")
                print(f"\033[90mRepository Name     :\033[0m \033[97m{repo['name']}\033[0m")
                print(f"\033[90mFull Name           :\033[0m \033[97m{repo['full_name']}\033[0m")
                print(f"\033[90mDescription         :\033[0m \033[97m{repo['description'] or 'Not Provided'}\033[0m")
                print(f"\033[90mOwner               :\033[0m \033[97m{repo['owner']['login']}\033[0m")
                print(f"\033[90mVisibility          :\033[0m \033[97m{repo['visibility'].title()}\033[0m")
                print(f"\033[90mPrimary Language    :\033[0m \033[97m{repo['language']}\033[0m")
                print(f"\033[90mDefault Branch      :\033[0m \033[97m{repo['default_branch']}\033[0m")
                print(f"\033[90mRepository Size     :\033[0m \033[97m{repo['size']} KB\033[0m")

                # URLs
                print("\n\033[96m[ Repository Links ]\033[0m")
                print(f"\033[90mGitHub URL          :\033[0m \033[94m{repo['html_url']}\033[0m")  # Blue for links
                print(f"\033[90mClone URL           :\033[0m \033[94m{repo['clone_url']}\033[0m")
                print(f"\033[90mSSH URL             :\033[0m \033[94m{repo['ssh_url']}\033[0m")

                # Activity Information
                print("\n\033[96m[ Activity ]\033[0m")
                print(f"\033[90mCreated On          :\033[0m \033[97m{repo['created_at'].split('T')[0]}\033[0m")
                print(f"\033[90mLast Updated        :\033[0m \033[97m{repo['updated_at'].split('T')[0]}\033[0m")
                print(f"\033[90mLast Push           :\033[0m \033[97m{repo['pushed_at'].split('T')[0]}\033[0m")

                # Statistics
                print("\n\033[96m[ Statistics ]\033[0m")
                print(f"\033[90mStars               :\033[0m \033[33m{repo['stargazers_count']}\033[0m")  # Yellow for stars
                print(f"\033[90mWatchers            :\033[0m \033[97m{repo['watchers_count']}\033[0m")
                print(f"\033[90mForks               :\033[0m \033[97m{repo['forks_count']}\033[0m")
                print(f"\033[90mOpen Issues         :\033[0m \033[97m{repo['open_issues_count']}\033[0m")

                # Features
                print("\n\033[96m[ Features ]\033[0m")
                print(f"\033[90mIssues Enabled      :\033[0m \033[97m{repo['has_issues']}\033[0m")
                print(f"\033[90mProjects Enabled    :\033[0m \033[97m{repo['has_projects']}\033[0m")
                print(f"\033[90mWiki Enabled        :\033[0m \033[97m{repo['has_wiki']}\033[0m")
                print(f"\033[90mPages Enabled       :\033[0m \033[97m{repo['has_pages']}\033[0m")
                print(f"\033[90mDiscussions Enabled :\033[0m \033[97m{repo['has_discussions']}\033[0m")

                # Repository Status
                print("\n\033[96m[ Status ]\033[0m")
                print(f"\033[90mArchived            :\033[0m \033[97m{repo['archived']}\033[0m")
                print(f"\033[90mDisabled            :\033[0m \033[97m{repo['disabled']}\033[0m")
                print(f"\033[90mTemplate Repository :\033[0m \033[97m{repo['is_template']}\033[0m")
                print(f"\033[90mForked Repository   :\033[0m \033[97m{repo['fork']}\033[0m")

                print("\033[34m" + "=" * 60 + "\033[0m\n\n")
        else:
            print("\033[31m  [!] An Unexpected error occurred!\033[0m")

    def analyze_commits(self):
        repos_url = self.url + f"users/{self.username}/repos"
        response = self.get_response(repos_url)
        if response:

            for index  ,  repo in enumerate(response ,start=1):
                repo_name = repo["name"]
                repo_url = repo["commits_url"].split("{")[0]    
                repo_commits =  self.get_response(repo_url)
                print("\n" + "=" * 60)
                print(f"{index}.  📦  {repo_name}")
                print("=" * 60)

                print(f"\nTotal Commits : {len(repo_commits)}")
                if len(repo_commits) < 20:
                    print("\nAll Commits")
                    print("-" * 15)
                    for index , commit in enumerate(repo_commits, start=1):
                        sha =commit["sha"]
                        message= commit["commit"]["message"]
                        date= commit["commit"]["author"]["date"]
                        print(f"\033[97m[{index}]\033[0m \033[96m[{sha}]\033[0m \033[90m{date}\033[0m \033[94m{message}\033[0m\n")
                    print("=" * 60+"\n\n")
                else:
                    print("\nRecent 20 Commits")
                    print("-" * 15)
                    for index , commit in enumerate(repo_commits[:20],start=1):
                        sha =commit["sha"]
                        message= commit["commit"]["message"]
                        date= commit["commit"]["author"]["date"]
                        print(f"\033[97m[{index}]\033[0m \033[96m[{sha}]\033[0m \033[90m{date}\033[0m \033[94m{message}\033[0m\n")
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
    # Bright Cyan for "GITHUB PROFILE"
    print("\033[96m")  
    print(r""" 
     ██████╗ ██╗████████╗██╗  ██╗██╗   ██╗██████╗     ██████╗ ██████╗  ██████╗ ███████╗██╗██╗    ███████╗    
    ██╔════╝ ██║╚══██╔══╝██║  ██║██║   ██║██╔══██╗    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝██║██║    ██╔════╝    
    ██║  ███╗██║   ██║   ███████║██║   ██║██████╔╝    ██████╔╝██████╔╝██║   ██║█████╗  ██║██║    █████╗      
    ██║   ██║██║   ██║   ██╔══██║██║   ██║██╔══██╗    ██╔═══╝ ██╔══██╗██║   ██║██╔══╝  ██║██║    ██╔══╝      
    ╚██████╔╝██║   ██║   ██║  ██║╚██████╔╝██████╔╝    ██║     ██║  ██║╚██████╔╝██║     ██║███████╗███████╗    
     ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝     ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚══════╝    
                                                                                                           """)
    # Bright Blue for "ANALYZER"
    print("\033[94m")  
    print(r"""
                █████╗ ███╗   ██╗ █████╗ ██╗  ██╗   ██╗███████╗███████╗██████╗ 
               ██╔══██╗████╗  ██║██╔══██╗██║  ╚██╗ ██╔╝╚══███╔╝██╔════╝██╔══██╗
               ███████║██╔██╗ ██║███████║██║   ╚████╔╝   ███╔╝ █████╗  ██████╔╝
               ██╔══██║██║╚██╗██║██╔══██║██║    ╚██╔╝   ███╔╝  ██╔══╝  ██╔══██╗
               ██║  ██║██║ ╚████║██║  ██║███████╗██║   ███████╗███████╗██║  ██║
               ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝""")
    
    print("\033[0m")  # reset formatting completely

    # Subtitle / Version Info with Cyan and Blue accents
    print("  \033[97mv1.0.0\033[0m  \033[90m|\033[0m  \033[96mGitHub API v2026\033[0m  \033[90m|\033[0m  \033[94mGemini 3.1 Flash Lite\033[0m\n")

    # Menu Options (White Action Keys, White Titles, Dark Gray Descriptions)
    print("  \033[90m--- \033[96mProfile \033[90m--------------------------------\033[0m")
    print("  \033[97m[1]\033[0m  \033[97mView Profile         \033[90mDisplay full GitHub user info\033[0m")
    print("  \033[97m[2]\033[0m  \033[97mRepository Stats     \033[90mDetailed breakdown of all repos\033[0m")
    print("  \033[97m[3]\033[0m  \033[97mCommit History       \033[90mBrowse recent commits per repo\033[0m")
    
    print("  \033[90m--- \033[96mAnalysis \033[90m-------------------------------\033[0m")
    print("  \033[97m[4]\033[0m  \033[97mAI Profile Summary   \033[90mFull career analysis with score  \033[94m[AI]\033[0m")
    
    print("  \033[90m--------------------------------------------\033[0m")
    print("  \033[31m[0]  Exit\033[0m\n")
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



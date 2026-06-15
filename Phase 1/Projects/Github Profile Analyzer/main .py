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
        repos_url = self.url + f"users/{self.username}/repos"
        response = self.get_response(repos_url)
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


    def analyze_commits(self):
        repos_url = self.url + f"users/{self.username}/repos"
        response = self.get_response(repos_url)
        for index  ,  repo in enumerate(response ,start=1):
            repo_name = repo["name"]
            repo_url = repo["commits_url"][:-6]
            repo_commits =  self.get_response(repo_url)
            print("\n" + "=" * 60)
            print(f"{index}.  📦{repo_name}")
            print("=" * 60)

            print(f"\nTotal Commits : {len(repo_commits)}")

            print("\nRecent Activity")
            print("-" * 15)
            for commit in repo_commits:
                sha =commit["sha"]
                message= commit["commit"]["message"]
                date= commit["commit"]["author"]["date"]
                print(f"[{sha}] {date}  {message}")
            print("=" * 60+"\n\n")


def get_username():
    pass


url="https://api.github.com/"








if __name__ == "__main__":
    pa= profile_analyzer("dawoodafzal62138", PATH , url , HEADERS)
    # pa.calculate_repository_stats()
    pa.analyze_commits()


import pathlib
import json
import requests
class profile_analyzer:
    def __init__(self, username , Path , Url ):
        self.username=  username
        self.path = Path
        self.url=Url




    def getrepos(self):
        pass

    def calculate_stars(self):
        pass





def get_username():
    pass




dir = pathlib.Path(__file__).parent.resolve() / "reports.json"
url="https://api.github.com/repos/dawoodafzal62138/issues"




r= requests.get(url)
print(r)

# if __name__ == "__main__":
#     pass
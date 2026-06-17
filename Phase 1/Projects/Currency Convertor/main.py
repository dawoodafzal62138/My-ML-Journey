import requests 
import json
from halo import Halo
import sys
import time


def typewritter(text , delay = 0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)



class currecny_convertor:
    def __init__(self , base_url):
        self.url = base_url


    def get_response(self , url):
        try:
            response = requests.get(url).json()
            return response
        except Exception as e:
            return {}


    def view_supported_currencies(self):
        supported_cuurency_url = self.url + "/codes"
        spinner = Halo("Fetching Codes ", "cyan", "blue" ,spinner="dots3")
        spinner.start()
        response = self.get_response(supported_cuurency_url)
        spinner.stop()
        if response:
            col = 3
            for index , codes in enumerate(response["supported_codes"] ,start=1):
                print(f"\033[32m [{index:>3}]  \033[1;34m{codes[0]} \033[0m: \033[36m{codes[1]:<30}" , end="")
                
                if index % col == 0:
                    print()
            print()





    def Convert_Currency():
        pass









API_KEY="4191ef346b1638d65d318a2c"
Base_url = f"https://v6.exchangerate-api.com/v6/{API_KEY}"




if __name__ == "__main__":
    c_obj = currecny_convertor(Base_url)
    c_obj.view_supported_currencies()
    # print("\033[32m index. \033[1;34m code \033[0m: \033[36m currency ")
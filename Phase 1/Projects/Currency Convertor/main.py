import requests 
import json
from halo import Halo
import sys
import time
import os

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
        else:
            typewritter("Something Wrong Happened :(")




    def Convert_Currency(self, from_, to  , amount):
        conversion_ur = self.url +f"pair/{from_.upper().strip()}/{to.upper().strip()}"
        response  = self.get_response(conversion_ur)
        rate = response.get("conversion_rate")
        total = amount * rate

        print("\n\033[34m" + "-" * 45 + "\033[0m")
        
        print(f"  \033[90mExchange Rate :\033[0m 1 \033[97m{from_}\033[0m = \033[96m{round(rate, 4)} {to}\033[0m")
        
        print(f"  \033[90mConversion    :\033[0m \033[97m{amount} {from_}\033[0m = \033[32m{round(total, 2)} {to}\033[0m")
        
        print("\033[34m" + "-" * 45 + "\033[0m\n")








API_KEY="4191ef346b1638d65d318a2c"
Base_url = f"https://v6.exchangerate-api.com/v6/{API_KEY}"


def menu():
   
    os.system("cls" if os.name=="nt" else "clear" )
    
    print(r"""
         ██████╗██╗   ██╗██████╗ ██████╗ ███████╗███╗   ██╗ ██████╗██╗   ██╗
        ██╔════╝██║   ██║██╔══██╗██╔══██╗██╔════╝████╗  ██║██╔════╝╚██╗ ██╔╝
        ██║     ██║   ██║██████╔╝██████╔╝█████╗  ██╔██╗ ██║██║      ╚████╔╝ 
        ██║     ██║   ██║██╔══██╗██╔══██╗██╔══╝  ██║╚██╗██║██║       ╚██╔╝  
        ╚██████╗╚██████╔╝██║  ██║██║  ██║███████╗██║ ╚████║╚██████╗   ██║   
         ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝   ╚═╝
        
     ██████╗ ██████╗ ███╗   ██╗██╗   ██╗███████╗██████╗ ████████╗ ██████╗ ██████╗ 
    ██╔════╝██╔═══██╗████╗  ██║██║   ██║██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
    ██║     ██║   ██║██╔██╗ ██║██║   ██║█████╗  ██████╔╝   ██║   ██║   ██║██████╔╝
    ██║     ██║   ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗   ██║   ██║   ██║██╔══██╗
    ╚██████╗╚██████╔╝██║ ╚████║ ╚████╔╝ ███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
     ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
    """)
    print("\n\033[34m" + "-" * 45 + "\033[0m")
    print("  \033[96mCURRENCY CONVERTER MENU\033[0m")
    print("\033[34m" + "-" * 45 + "\033[0m")

    print("  \033[97m[1]\033[0m  \033[97mView Supported Currencies\033[0m")
    print("  \033[97m[2]\033[0m  \033[97mConvert Currency\033[0m")
    print("  \033[31m[3]  Exit\033[0m")
    
    print("\033[34m" + "-" * 45 + "\033[0m\n")
    choice = input("  \033[96mEnter choice ›\033[0m ").strip()
    return choice




   


if __name__ == "__main__":
    c_obj = currecny_convertor(Base_url)
    # # c_obj.view_supported_currencies()
    # # print("\033[32m index. \033[1;34m code \033[0m: \033[36m currency ")
    # c_obj.Convert_Currency("usd", "pkr" , 3.10)
    action = { 
        "1": c_obj.view_supported_currencies,
        "2": c_obj.Convert_Currency,
        "3": exit
    }
                    



    menu()
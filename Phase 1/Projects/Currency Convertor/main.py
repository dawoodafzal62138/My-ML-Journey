import requests 
from halo import Halo
import os
import sys





class currency_convertor:
    def __init__(self , base_url):
        self.url = base_url


    def get_response(self , url):
        spinner = Halo("Fetching Codes ", "cyan", "blue" ,spinner="dots3")
        spinner.start()
        try:
            response = requests.get(url).json()
            
            if "error-type" in response.keys():
                return f"\tError :\033[31m  {response['error-type']}\n" 
            return response

        except requests.exceptions.MissingSchema:
            return "Error: Invalid URL (missing http/https)"

        except requests.exceptions.ConnectionError:
            return "Error: Cannot connect to server"

        except requests.exceptions.Timeout:
            return "Error: Request timed out"

        except requests.exceptions.HTTPError as e:
            return f"HTTP Error: {e}"

        except ValueError:
            return "Error: Response is not valid JSON"
        finally:
            spinner.stop()



    def view_supported_currencies(self):
        supported_cuurency_url = self.url + "/codes"
        response = self.get_response(supported_cuurency_url)
        if isinstance(response , dict):
            col = 3
            for index , codes in enumerate(response["supported_codes"] ,start=1):
                print(f"\033[32m [{index:>3}]  \033[1;34m{codes[0]} \033[0m: \033[36m{codes[1]:<30}" , end="")
                
                if index % col == 0:
                    print()
            print()
        else:
            print(response)




    def convert_currency(self):
        from_= input("  \033[97m[1]\033[0m  \033[97m Enter the source Currency Code  : \033[0m").upper().strip()
        to = input("  \033[97m[2]\033[0m  \033[97m Enter the target Currency Code  : \033[0m").upper().strip()
        while True:
            try:
                amount = float(input("  \033[97m[3]\033[0m  \033[97m Enter the Amount                : \033[0m"))
                if amount > 0:
                    conversion_url = self.url +f"/pair/{from_.upper().strip()}/{to.upper().strip()}"
                    response  = self.get_response(conversion_url)
                    if isinstance(response , dict):
                            rate = response.get("conversion_rate")
                            total = amount * rate

                            print("\n\033[34m" + "-" * 45 + "\033[0m")
                            
                            print(f"  \033[90mExchange Rate :\033[0m 1 \033[97m{from_}\033[0m = \033[96m{round(rate, 4)} {to}\033[0m")
                            
                            print(f"  \033[90mConversion    :\033[0m \033[97m{amount} {from_}\033[0m = \033[32m{round(total, 2)} {to}\033[0m")
                            
                            print("\033[34m" + "-" * 45 + "\033[0m\n")
                    else:
                        print(response)
                    break
                else:
                    print("\n\033[31m \tAmount Can't be Negative\n")
            except ValueError:
                print("\t\033[31m Invalid Input !")



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
    # The API key should be enclosed in String
    API_KEY="Your-API-Key"

    Base_url = f"https://v6.exchangerate-api.com/v6/{API_KEY}"
    
    c_obj = currency_convertor(Base_url)
    action = { 
        "1": c_obj.view_supported_currencies,
        "2": c_obj.convert_currency,
        "3": sys.exit
    }
    while True:
        choice = menu()
        if choice in action.keys():
            action[choice]()
            input("\n  \033[34m Press Enter to return to menu...")
        else: 
            print("\033[31m     Invalid Choice !")     



   
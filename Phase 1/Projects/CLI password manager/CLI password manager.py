import getpass
from cryptography.fernet import Fernet
import hashlib
import base64
import pathlib
import json
class password_manager:
    def __init__(self,account):
        self.account = account
        self.path=pathlib.Path("Phase 1/Projects/CLI password manager/password.json")
        master_key = self.read_data_json()[self.account]["master key"]
        self.master_key=Fernet(master_key)

    def read_data_json(self):
        with self.path.open("r") as f:
            data= json.load(f)
        return data    

    def write_data_json(self,data):
        with self.path.open("w") as f:
            json.dump(data ,f , indent=4)

    def search(self ,acc_name):
        data= self.read_data_json()
        if acc_name.lower().strip() in data[self.account]["passwords"].keys():
            return True
        return False
    
    def add_password(self , acc_name , password):
        if not self.search(acc_name):
        
            data=self.read_data_json()
            password = self.master_key.encrypt(password.encode()).decode()
        
            data[self.account]["passwords"][acc_name.lower().strip()] = password
            self.write_data_json(data)
            success(f"Password for '{acc_name}' added successfully 🔑")
        
        else:
            
            error("This account already exists!")

        
        


    def get_password(self ,acc_name):
        if  self.search(acc_name):
            data= self.read_data_json()
            print(f" 🌐 {acc_name}'s Password → 🔑 {self.master_key.decrypt(data[self.account]["passwords"][acc_name]).decode()}")
        else: 
            error(f"Account '{acc_name}' not found!")





    def list_password(self):
        data = self.read_data_json()
        i=1
        print("\n" + "="*50)
        print("📜 STORED PASSWORDS")
        print("="*50)
        for key , value in data[self.account]["passwords"].items():
            print(f"{i}. 🌐 {key} → 🔑 {self.master_key.decrypt(value).decode()}")
            i+=1

    def delete_password(self):
        data = self.read_data_json()
        i=1
        print("\n" + "-"*40)
        print("🗑 Available Accounts")
        print("-"*40)
        for key in data[self.account]["passwords"].keys():
            print(f"{i}. Account Name : {key}")
            i+=1
        acc_name= input("Enter Account name you want to delete ! ")
        if self.search(acc_name):
            del data[self.account]["passwords"][acc_name.lower().strip()]
            self.write_data_json(data)
            success("Password deleted successfully 🗑")
        else:
            print("This account doesn't Exists ! ")



path=pathlib.Path("Phase 1/Projects/CLI password manager/password.json")

def read():
    try: 
        with path.open("r") as f:
            data = json.load(f)
    except :
        data = {}
    return data


def create_master_password(username , master_password):

    data = read()

    K=base64.urlsafe_b64encode(hashlib.sha256(master_password.encode()).digest()) 
    data.update({username : {"master key": K.decode() ,"passwords": {}}})
    with path.open("w") as f:
        json.dump(data ,f ,indent = 4)
        success("Account created successfully 🎉")


def error(msg):
    print("\n" + "❌ " + msg + "\n")

def success(msg):
    print("\n" + "✔ " + msg + "\n")

def choices_after_login(account):
    P_M = password_manager(account)
    while True:
        try:
            print("\n" + "-"*50)
            print(f"👤 Logged in as: {account}")
            print("-"*50)
            print("1. ➕ Add Password")
            print("2. 🔍 Get Password")
            print("3. 📜 List All Passwords")
            print("4. ❌ Delete Password")
            print("5. 🚪 Exit")
            print("-"*50)
            choices = int(input("\n Choice: "))
            if choices == 1: 
                acc_name= input("Enter the account Name: " )
                password = getpass.getpass(prompt="Enter password: ", echo_char= "*")
                password2 = getpass.getpass(prompt="Confirm password: " ,echo_char="*")
                if password == password2:
                    P_M.add_password(acc_name,password)
                else:
                    print("Passwords doesn't Match")

            elif choices == 2 :
                acc_name= input("Enter Account Name:")
                P_M.get_password(acc_name)
        
            elif choices == 3:
                P_M.list_password()
        
            elif choices == 4:
                P_M.delete_password()

            elif choices == 5:
                exit()   
        
        except ValueError:
            print("Invalid Choice ! ")

    



def choices_menu():
    while True:
        try:
            print("\n" + "="*50) 
            print("🔐        CLI PASSWORD MANAGER        🔐")
            print("="*50)
            print("\n1. Login\n2. Sign up\n3. Exitn\n Choice : ")
            print("="*50)
            choice = int(input("\nChoice: "))
            if choice == 1 :
                login_username =input("\nEnter Your Username: ")
                password =getpass.getpass(prompt="\nEnter the password: " ,echo_char="*")
                K=base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest()) 
                data = read()
                if login_username in data.keys() and  K.decode() == data[login_username]["master key"]:
                      success("Login Successful! Welcome back 🔐")
                      choices_after_login(login_username)
                else:
                  
                    error("Incorrect Username or password :(")
            elif choice == 2 :
                data = read()
                username = input("\nEnter your Username: ") 
                if not username in data.keys():
                    pass1 = getpass.getpass(prompt="\nEnter your Password: " ,echo_char="*") 
                    pass2 = getpass.getpass(prompt="\nConfirm password : " ,echo_char="*") 
                    if pass1.__eq__(pass2) :
                        
                        create_master_password(username , pass1)
                
                else:
                    print("\nAccount ALready exists !")
            elif choice == 3:
                exit()
                
        except ValueError  :
            print("Invalid Choice ! ")


if __name__ == "__main__":
    print("\n" + "🟦"*25)
    print("      WELCOME TO PASSWORD MANAGER")
    print("🟦"*25)
    print("     Secure • Simple • Fast 🔐")
    print("🟦"*25 + "\n")
    choices_menu() 




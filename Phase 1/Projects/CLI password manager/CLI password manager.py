from cryptography.fernet import Fernet
import hashlib
import base64
import pathlib
import json
class password_manager:
    def __init__(self):
        
        self.path=pathlib.Path("Phase 1/Projects/CLI password manager/password.json")
        master_key = self.read_data_json()["master key"]
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
        for key in data["passwords"].keys():
            if key == acc_name.lower().strip():
                return False
        return True
    
    def add_password(self , acc_name , password):
        password = self.master_key.encrypt(password.encode()).decode()
        
        data=self.read_data_json()
        
        data["passwords"][acc_name.lower().strip()] = password
        # if self.search() == False:
        self.write_data_json(data)
        print(f"Password of {acc_name} added Succesfully")


    def get_password(self):
        pass

    def list_password(self):
        pass

    def delete_password(self):
        pass


def create_master_password(master_password):
    K=base64.urlsafe_b64encode(hashlib.sha256(master_password.encode()).digest()) 
    sha_key = {"master key": K.decode() ,"passwords": {}}
    path=pathlib.Path("Phase 1/Projects/CLI password manager/password.json")
    with path.open("w") as f:
        json.dump(sha_key ,f ,indent = 4)

    return K


if __name__ == "__main__":
    
    # create_master_password("dawood")
    p_m = password_manager()
    # p_m.add_password("google", "Smart@1122")

    print(p_m.search("google"))
    
import json
import argparse
import datetime
import pathlib
import os


class Task:
    def __init__(self , id: int , title : str, status : str , created_at ):
        self.id = id
        self.title = title
        self.status = status
        self.created_at = created_at



class TaskManager:
    def __init__(self , path : str):
        self.path = path

    def load_task(self):
        try:

            with self.path.open("r") as f: 
                data= json.load(f)
                return data
        except (json.JSONDecodeError , FileNotFoundError):
            return []            


    def get_next_id(self):
        data = self.load_task()
        if not data:
            return 1
        return max([item["id"] for item in data]) + 1

    def add_task(self  , title : str, status : str , created_at ):

        id = self.get_next_id()
        t= Task( id , title , status, created_at )
        self.data= vars(t)
        self.save_task()

    
    
    def save_task(self):
        data = self.load_task()
        data.append(self.data)
        with self.path.open("w" ) as f:
            json.dump(data, f ,indent=4)


    def delete_task(self):
        pass
    def compelete_task(self):
        pass



    def list_tasks(self):
        pass



PATH  = pathlib.Path(__file__).parent.resolve() / "data.json"

if __name__ == "__main__":
    tm = TaskManager(PATH)
    tm.add_task( "buy groceries"  , "pending" , str(datetime.datetime.now()))

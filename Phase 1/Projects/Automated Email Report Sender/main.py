import csv
import pathlib
import json


class Data:
    def __init__(self , path ):
        self.path = path 


    def read_csv(self):
        categories = []
        with self.path.open("r") as f:
            data  = csv.DictReader(f)
            for line in list(data)[:32]:
                for key , value in line.items():


    def response_ai(self):
        pass









if __name__ == "__main__":
    path = pathlib.Path(__file__).parent.resolve() / "Online Sales Data kaggle.csv"
    d = Data(path)
    d.read_csv()


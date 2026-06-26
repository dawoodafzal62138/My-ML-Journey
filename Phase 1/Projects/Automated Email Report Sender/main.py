import csv
import pathlib
import json


class Data:
    def __init__(self , path ):
        self.path = path 


    def read_csv(self):
        filtered_data = []
        with self.path.open("r") as f:
            data  = csv.DictReader(f)
            list_ = ["Product Category" ,"Units Sold" ,"Unit Price" ,"Total Revenue" ,"Region"]
            for line in list(data)[:32]:
                category = {}
                for key , value in line.items():
                    if key in list_:
                        category[key] = value
                    
                filtered_data.append(category)
        return filtered_data 
    
    
    def organize_data(self):
        data = self.read_csv()

        sorted_data = sorted(
            data,
            key=lambda item: (
                item["Product Category"],
                item["Region"]
            )
        )
        return sorted_data
    


    def response_ai(self):
        pass









if __name__ == "__main__":
    path = pathlib.Path(__file__).parent.resolve() / "Online Sales Data kaggle.csv"
    d = Data(path)
    d.organize_data()


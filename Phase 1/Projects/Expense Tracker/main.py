import csv , datetime , pathlib , random 
import customtkinter as tk

SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()
FILE_PATH = SCRIPT_DIR / "expenses.csv"
HEADERS=[ "Date" , "Type" , "Amount" , "Category" , "Description"]

if not FILE_PATH.exists():
    FILE_PATH.touch()
    with FILE_PATH.open("w" , newline="") as f:
        csv_writer= csv.DictWriter(f, fieldnames= HEADERS ,delimiter=",")
        csv_writer.writeheader()
        



class expense_tracker:
    def __init__(self):
        self.path  = FILE_PATH

    def write_csv(self , date , type , amount , category , description ):
        with self.path.open("a", newline="") as f:

            text={"Date" : date, "Type": type , "Amount" : amount, "Category" : category, "Description": description}
            csv_writer= csv.DictWriter(f, fieldnames= HEADERS, delimiter=",")
           
            csv_writer.writerow(text)

    def add_expense_income(self, date, type , amount , category , description):
        self.write_csv(date, type , amount, category,description)    

    def list_incomes(self, type = "all" ):
        with self.path.open("r" ,newline="") as f :
            csv_reader = csv.DictReader(f , delimiter=",")
            yield list(csv_reader.fieldnames)
            for line in csv_reader:
                if type.lower() == "all":
                    
                    yield list(line.values())
                else:
                    if line["Type"].lower() == type.lower().strip():
                        yield list(line.values())

               


    def summary (self):
        expenses= 0
        income= 0
        
        try:
            with self.path.open("r" ,newline="") as f :
                csv_reader = csv.DictReader(f , HEADERS ,delimiter=",")
                next(csv_reader)
                for line in csv_reader:
                    if line["Type"].lower() == "income":
                        income += float(line["Amount"])
                    elif line["Type"].lower() == "expense":
                        expenses += float(line["Amount"])
        except :
            pass 
                    
                    
          
        return income , expenses , income - expenses












income_categories = [
    "Salary",
    "Bonus",
    "Freelance",
    "Business",
    "Part-time Job",
    "Overtime",
    "Commission",
    "Investment",
    "Dividends",
    "Interest",
    "Rental Income",
    "Royalties",
    "Pension",
    "Scholarship",
    "Grant",
    "Gift Received",
    "Refund",
    "Cashback",
    "Tax Refund",
    "Lottery",
    "Insurance Claim",
    "Sale of Assets",
    "Side Hustle",
    "YouTube",
    "Affiliate Marketing",
    "Online Course Sales",
    "Crypto Profit",
    "Stock Profit",
    "Other Income"
]

expense_categories = [
    "Food",
    "Transport",
    "Rent",
    "Utilities",
    "Shopping",
    "Health",
    "Education",
    "Entertainment",
    "Travel",
    "Personal Care",
    "Bills",
    "Insurance",
    "Taxes",
    "Gift",
    "Investment",
    "Other"
]


exp = expense_tracker()
# for _ in range(100): 
#         exp.add_expense(datetime.datetime.now() ,random.randint(1000,10000) , random.choice(expense_categories) ,  "")
# #         exp.add_income(datetime.datetime.now() ,random.randint(1000,10000) , random.choice(income_categories) ,  "")
# print(list(exp.list_incomes()))

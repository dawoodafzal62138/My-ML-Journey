import csv , datetime , pathlib , random 
import customtkinter as tk

SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()
FILE_PATH = SCRIPT_DIR / "expenses.csv"
HEADERS=[ "date" , "type" , "amount" , "category" , "description"]

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

            text={"date" : date, "type": type , "amount" : amount, "category" : category, "description": description}
            csv_writer= csv.DictWriter(f, fieldnames= HEADERS, delimiter=",")
           
            csv_writer.writerow(text)

    def add_expense_income(self, date, type , amount , category , description):
        self.write_csv(date, type , amount, category,description)    

    def list_incomes(self, type = "all" ):
        list_payments=[]
        with self.path.open("r" ,newline="") as f :
            csv_reader = csv.DictReader(f , HEADERS ,delimiter=",")
            # next(csv_reader)
            for line in csv_reader:
                if type == "all":
                    
                    yield list(line.values())
                else:
                    if line["type"].lower() == type.lower().strip():
                        yield list(line.values())

               


    def monthly_report(self):
            pass
    





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

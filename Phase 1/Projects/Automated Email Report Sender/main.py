import csv
import pathlib
from google import genai
from google.genai import errors
from dotenv import load_dotenv
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



class Data:
    def __init__(self , path , api , system_prompt):
        self.path = path    
        self.GEMINI_API = api
        self.system_path = system_prompt
        



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
        data = self.organize_data()
        if os.path.exists(self.system_path):
            with self.system_path.open("r") as f:
                prompt = f.read()
        else:
            prompt = ""


        try:
            client = genai.Client(api_key=self.GEMINI_API)
            session = client.chats.create(model ="gemini-3.1-flash-lite" , config={"system_instruction": prompt})
            response = session.send_message(str(data))
    
            return response.text
        except errors.ClientError as e:
            return f"Error: {e}"





def send_email(APP_PASSWORD , response):
    # 1. Email Configuration
    smtp_server = "smtp.gmail.com"  # Example using Gmail
    smtp_port = 587                 # Standard port for TLS
    
    # senders gmail address
    sender_email = "example@gmail.com"
    
    sender_password = APP_PASSWORD # Use an App Password, not your real password!
    
    
    
    # recievers gmail address
    receiver_email = "example@gmail.com"

    # 2. Construct the Email Message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    # Subject
    message["Subject"] = "Daily Sales Report"

    # Create the body of the email

    body = response
    message.attach(MIMEText(body, "plain"))

    # 3. Connect to the Server and Send
    try:
        # Establish a secure session with the server
        print("Connecting to server...")
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls() # Secure the connection
            
            # Login to your email account
            server.login(sender_email, sender_password)
            print("Login successful!")
            
            # Send the email
            # We convert the MIME message object to a string before sending
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully!")
            
    except Exception as e:
        print(f"An error occurred: {e}")






if __name__ == "__main__":

    load_dotenv()
    GEMINI_API = os.getenv("GEMINI_API")
    APP_PASSWORD = os.getenv("APP_PASSWORD")
    
    DATA_PATH = pathlib.Path(__file__).parent.resolve() / "Online Sales Data kaggle.csv"
    PROMPT_PATH = pathlib.Path(__file__).parent.resolve() / "prompt.txt"

    d = Data(DATA_PATH , GEMINI_API ,PROMPT_PATH)
    response = d.response_ai()
    send_email( APP_PASSWORD, response)




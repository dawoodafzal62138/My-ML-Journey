from customtkinter import * 
from CTkMessagebox import CTkMessagebox
from google import genai
class gui:
    def __init__(self):
        self.app = CTk()
        self.app.minsize(1100 , 700)
        self.app.geometry("1100X700+1000+600")
        self.app.resizable(False ,False)
        self.__api_key =None
        self.main_window()


        self.app.mainloop()


    # def response_AI():
    #     client =genai.Client(api_key=)


    def main_window(self):
        title_label = self.label("Text-Based Adventure Game ! ", 0.5 , 0.1 ,self.app , font = CTkFont("seogi UI", 40 ,"bold") ,text_color="#EAEAEA")


        text_box = self.textarea(800 ,475, 0.5,0.50 ,self.app ,border_color = "#3C3C3C", border_width = 3 ,corner_radius= 10 , bg_color="#252526" ,text_color="#1BD53A" , font=CTkFont(family="Segoe UI Emoji", size=14) ,wrap ="word")
        

        entry_bar = self.entry(650, 50 ,"Enter your Choice" , 0.432 ,0.9 ,self.app , fg_color= "#2B2B2B" ,text_color = "#FFFFFF" ,border_width =3 , corner_radius =10 ,border_color ="#3C3C3C" ,font = CTkFont("Seogi UI" ,20  ,weight= "bold" ))

        enter_button= self.button(130 ,50 ,"Enter" , 0.805 ,0.9 ,self.app ,fg_color ="#222222"  ,text_color="#39FF14" ,border_width = 3 ,border_color="#3C3C3C", corner_radius = 10,font = CTkFont("Seogi UI" ,20  ,weight= "bold" ), hover_color= "#333333")

        if not self.__api_key:
            inputdialog = CTkInputDialog(title="GET GEMINI API KEY" , text="Enter your Gemini API Key")

        




    def button(self , width_ , height_ ,text_, pad_x_ ,pad_y_, master, **kwargs):
        button1=CTkButton(master= master, width=width_, height=height_, text=text_,  **kwargs)
        button1.place(relx= pad_x_ ,rely= pad_y_ ,anchor ="center")
        return button1



    def label(self ,text_, pad_x_ ,pad_y_,  master , **kwargs):
        label=CTkLabel(master= master, text=text_, **kwargs)
        label.place(relx =pad_x_ ,rely=pad_y_ ,anchor ="center")
        return label


    def entry(self, width_ , height_ ,text_, pad_x_ ,pad_y_,  master , **kwargs):
        entry=CTkEntry(master= master, width=width_, height=height_, placeholder_text=text_, **kwargs)
        entry.place(relx= pad_x_ ,rely= pad_y_ , anchor ="center")
        return entry



    def textarea(self , width_ , height_ , pad_x_ ,pad_y_,  master , **kwargs):
        textarea_=CTkTextbox(master= master, width=width_, height=height_, **kwargs)
        textarea_.place(relx =pad_x_,rely= pad_y_ , anchor = "center" )
        textarea_.configure(state ="normal")
        return textarea_





g = gui() 

























































































































































































# import customtkinter as ctk

# root = ctk.CTk()
# root.geometry("800x600")
# root.title("RPG Layout")

# # 1. CONFIGURE THE GRID WEIGHTS (The "invisible skeleton")
# root.columnconfigure(0, weight=0)   # Left sidebar (fixed)
# root.columnconfigure(1, weight=3)   # Main story (grows massive)
# root.columnconfigure(2, weight=1)   # Stats/Inventory (grows a little)

# root.rowconfigure(0, weight=0)      # Title bar (fixed height)
# root.rowconfigure(1, weight=2)      # Story box (grows tall)
# root.rowconfigure(2, weight=1)      # Choices (grows a little)
# root.rowconfigure(3, weight=0)      # Input bar (fixed height)

# # 2. PLACE WIDGETS AND USE STICKY (The "meat on the bones")

# # ROW 0
# title_label = ctk.CTkLabel(root, text="SCENE TITLE", fg_color="gray30")
# # spans across column 1 and 2, stretches horizontally
# title_label.grid(row=0, column=1, columnspan=2, sticky="ew", padx=5, pady=5) 

# # ROW 1
# story_output = ctk.CTkTextbox(root)
# # "nsew" makes it fill the massive weight=2 / weight=3 cell entirely
# story_output.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

# stats_frame = ctk.CTkFrame(root, fg_color="darkred")
# stats_frame.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)

# # ROW 2
# choices_frame = ctk.CTkFrame(root, fg_color="darkblue")
# choices_frame.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

# inventory_frame = ctk.CTkFrame(root, fg_color="darkgreen")
# inventory_frame.grid(row=2, column=2, sticky="nsew", padx=5, pady=5)

# # ROW 3
# command_input = ctk.CTkEntry(root, placeholder_text="Type a command...")
# command_input.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

# root.mainloop()
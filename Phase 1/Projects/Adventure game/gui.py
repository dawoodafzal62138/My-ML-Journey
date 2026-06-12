from customtkinter import * 
from google import genai
class gui:
    def __init__(self):
        self.app = CTk()
        self.app.minsize(1100 , 700)
        self.app.resizable(False ,False)
        # self.__api_key =
        self.main_window()


        self.app.mainloop()


    # def response_AI():
    #     client =genai.Client(api_key=)


    def main_window(self):
        title_label = self.label("Text-Based Adventure Game ! ", 0.5 , 0.1 ,self.app , font = CTkFont("seogi UI", 40 ,"bold") ,text_color="#EAEAEA")


        text_box = self.textarea(800 ,400, 0.5,0.45 ,self.app ,border_color = "#3C3C3C", border_width = 3 ,corner_radius= 10 , bg_color="#252526" ,text_color="#1BD53A" , font=CTkFont(family="Segoe UI Emoji", size=14) ,wrap ="word")
        

        entry_bar = self.entry(650, 50 ,"Enter your Choice" , 0.432 ,0.8 ,self.app , fg_color= "#2B2B2B" ,text_color = "#FFFFFF" ,border_width =3 , corner_radius =10 ,border_color ="#3C3C3C" ,font = CTkFont("Seogi UI" ,20  ,weight= "bold" ) , placeholder_text_color ="#555555")

        enter_button= self.button(130 ,50 ,"Enter" , 0.805 ,0.8 ,self.app ,fg_color ="#252526"  ,text_color="#FFFFFF" ,border_width = 3 ,border_color="#3C3C3C", corner_radius = 10,font = CTkFont("Seogi UI" ,20  ,weight= "bold" ), hover_color= "#39FF14")

        text_box.insert(index=0.0 ,text="""🎮 NEW ADVENTURE
🎭 Genre:
Cyberpunk Noir
🌎 Setting:
Neo-Veridia, a rain-slicked, neon-drenched megacity built over the ruins of the Old World.
🌫️ Atmosphere:
Oppressive, gritty, rain-soaked, and buzzing with electric tension.
🎯 MAIN GOAL:
Retrieve the encrypted Data-Shard 💾 stolen from the Arasaka-Kovacs vault before the local syndicate, The Neon Skulls, cracks the security.
⚠️ DANGER LEVEL:
High

📖 INTRODUCTION
The relentless acid rain 🌧️ sizzles against your synthetic leather jacket as you crouch on the fire escape of a decaying skyscraper. Below, the streets of Neo-Veridia are a kaleidoscope of holographic advertisements 🏮 reflecting in deep, oil-slicked puddles. You adjust the strap of your holstered heavy pistol 🔫; it’s the only thing that’s kept you breathing this long. Your side feels bruised from a rough landing earlier, a nagging 🩹 reminder that your mission is already behind schedule. Your HUD flickers with a low-battery warning—you’ve only got your trusty multitool 🛠️ and a single thermal charge 💣 to your name. Somewhere in the sprawling industrial district ahead, the data-shard 💾—your ticket to early retirement—is being decrypted by a syndicate hacker. You can smell the ozone from the nearby power conduits and the rot of the lower city. It’s time to move before the window of opportunity closes for good.

📍 TURN 1/15
🎯 OBJECTIVE
Infiltrate the Neon Skulls' hideout and retrieve the stolen Data-Shard.

⚡ CHOICES
1️⃣ Rappel down the side of the building to enter through the ventilation shaft on the lower level.
2️⃣ Hack the exterior security node to disable the perimeter cameras and sneak through the front loading dock.
3️⃣ Try to bribe a patrolling low-level guard standing by the service entrance with your last credit chip.
4️⃣ Use your thermal charge 💣 to blow a hole in the roof and jump straight into the heart of the facility.

⌨️ What do you do?""")




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
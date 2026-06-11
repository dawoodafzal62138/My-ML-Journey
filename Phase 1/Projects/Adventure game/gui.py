import customtkinter as tk
class gui:
    def __init__(self):
        self.app = tk.CTk()
        self.app.minsize(1100 , 700)
        self.app.resizable(True ,True)
        self.app.grid = 
        self.app.mainloop()






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
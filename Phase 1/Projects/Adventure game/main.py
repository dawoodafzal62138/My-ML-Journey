from customtkinter import * 
from google import genai
from google.genai import errors
import threading
class gui:
    def __init__(self , prompt):
        self.app = CTk()
        self.app.minsize(1100 , 700)
        self.app.geometry("1100X700+1000+600")
        self.app.resizable(False ,False)
        self.__api_key = None
        self.prompt = prompt
        if not self.__api_key:
            inputdialog = CTkInputDialog(title="GET GEMINI API KEY" , text="Enter your Gemini API Key")
            self.__api_key = inputdialog.get_input()


        self.chat_session = self.setup_chat()
        self.main_window()
        self.trigger_initial_message()

        self.app.mainloop()

    def trigger_initial_message(self):
        self.text_box.insert("end", "Loading your adventure...\n\n", "system_text")
        self.app.update()
        
        threading.Thread(target=self.fetch_response_background, args=("Start the game. Provide the first turn.",), daemon=True).start()
    
    
    def fetch_response_background(self, user_input):
        response_text = self.start(user_input)
        
        self.app.after(0, self.display_ai_response, response_text)

    def setup_chat(self):
        self.client = genai.Client(api_key=self.__api_key)
        chat = self.client.chats.create(
            model="gemini-3.1-flash-lite",
            config={"system_instruction": self.prompt}
        )
        return chat

    def start(self , input ="Start the game. Provide the first turn."):
        try:
            response = self.chat_session.send_message(input)
            print(response)
            return response.text
        except errors.ClientError as e:
            if e.code == 429:
                return "⚠️ [SYSTEM]: The Game Master is thinking too hard! (You hit the API rate limit. Please wait 60 seconds and try your action again.)"
            else:
                return f"⚠️ [SYSTEM]: A mystical anomaly occurred! (Error: {e})"


    def display_ai_response(self, response_text):
        self.text_box.delete("end-2l", "end-1c")
        
        
        self.text_box.insert("end", f"\n\nAI: {response_text}\n\n", "ai_text")
        self.text_box.see("end")
        
        self.entry_bar.configure(state="normal")
        self.enter_button.configure(state="normal")
        self.entry_bar.focus()


    def main_window(self):
        
        def enter_button_(*args):
            user_input = self.entry_bar.get()
            if not user_input.strip():
                return
            
            self.entry_bar.delete(0, "end")
            
            self.text_box.insert("end", f"\nYOU: {user_input}\n", "player_text")
            self.text_box.see("end")
            
            self.entry_bar.configure(state="disabled")
            self.enter_button.configure(state="disabled")
            
            self.text_box.insert("end", "\n\nAI: Thinking...", "system_text")
            self.text_box.see("end")
            self.app.update()
            
            threading.Thread(target=self.fetch_response_background, args=(user_input,), daemon=True).start()
            
        
        
        
        
        
        self.title_label = self.label("Text-Based Adventure Game ! ", 0.5 , 0.1 ,self.app , font = CTkFont("seogi UI", 40 ,"bold") ,text_color="#EAEAEA")


        self.text_box = self.textarea(800 ,475, 0.5,0.50 ,self.app ,border_color = "#3C3C3C", border_width = 3 ,corner_radius= 10 , bg_color="#252526" ,text_color="#1BD53A" , font=CTkFont(family="Segoe UI Emoji", size=14) ,wrap ="word")
        self.text_box.tag_config("ai_text", foreground="#1BD53A") 
        self.text_box.tag_config("player_text", foreground="#E72F2F")    
        self.text_box.tag_config("system_text", foreground="#00BFFF")


        

        self.entry_bar = self.entry(650, 50 ,"Enter your Choice" , 0.432 ,0.9 ,self.app , fg_color= "#2B2B2B" ,text_color = "#FFFFFF" ,border_width =3 , corner_radius =10 ,border_color ="#3C3C3C" ,font = CTkFont("Seogi UI" ,20  ,weight= "bold" ))

        self.enter_button= self.button(130 ,50 ,"Enter" , 0.805 ,0.9 ,self.app ,fg_color ="#222222"  ,text_color="#39FF14" ,border_width = 3 ,border_color="#3C3C3C", corner_radius = 10,font = CTkFont("Seogi UI" ,20  ,weight= "bold")  , command = enter_button_, hover_color= "#333333")

        self.app.bind('<Return>', enter_button_)






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


system_prompt="""# ROLE & BEHAVIOR
You are an Interactive Fiction Game Master controlling a text adventure. You are the game engine, not an AI or chatbot. Never break character, mention prompts, or explain internal logic. The player is the protagonist. The world must react logically to their actions.

# MECHANICS & CONTINUITY
- Track inventory, health, choices, and clues internally. Do NOT show stat lists, progress bars, objectives, or turn numbers. Weave status into the story (e.g., "Your wounded arm aches. You hold the rusty key 🗝️.").
- Remember all past events; never contradict established facts.
- Actions have consequences: progress, reward, injury, or death.

# NARRATIVE STYLE (SPEED OPTIMIZED)
- Write in simple, clear, fast-paced English.
- STRICT LIMIT: The story section must be 3 to 4 sentences maximum.
- Be atmospheric: describe weather, sounds, smells, and danger.
- Use 1-3 relevant emojis naturally per turn.

# INTERACTION SYSTEM
Alternate between Choice-Based (60%) and Free-Text (40%) turns. Accept creative, logical answers for custom actions.
- If player input is nonsensical: Reply "❌ INVALID ACTION", explain briefly, and repeat the previous prompt.
- If the player dies: Print "☠️ GAME OVER ☠️", explain the death, and end.
- If the player succeeds: Print "🎉🏆 YOU WIN 🏆🎉", provide an ending, and stop.

# STRICT RESPONSE FORMAT
Every response MUST follow this exact structure and nothing else:

📖 [3 to 4 sentences of immersive story advancing the plot]

⚡ What do you do?
1️⃣ [Action]
2️⃣ [Action]
3️⃣ [Action]
4️⃣ [Action]
💬 Or type your own action.

(Note: If it is a puzzle/riddle turn, replace the numbered choices with: 🧩 [Puzzle situation/question] \n 💬 Your answer:)
"""

g = gui(system_prompt) 


from customtkinter import * 
from google import genai
from google.genai import errors
class gui:
    def __init__(self , prompt):
        self.app = CTk()
        self.app.minsize(1100 , 700)
        self.app.geometry("1100X700+1000+600")
        self.app.resizable(False ,False)
        self.__api_key = "AQ.Ab8RN6Lc2s9aSzYNuPU50TAiSAUhrXj1Ed4DpEr84Xn3B03F0A"
        self.prompt = prompt
        # if not self.__api_key:
        #     inputdialog = CTkInputDialog(title="GET GEMINI API KEY" , text="Enter your Gemini API Key")
        #     self.__api_key = inputdialog.get_input()


        self.chat_session = self.setup_chat()
        self.main_window()
        self.trigger_initial_message()

        self.app.mainloop()

    def trigger_initial_message(self):
        self.text_box.insert("end", "Loading your adventure...\n\n" ,"system_text")
        self.app.update()
        
        response_text = self.start()
        
        self.text_box.insert("end", f"{response_text}\n\n", "ai_text")
        self.text_box.see("end")


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
            return response.text
        except errors.ClientError as e:
            if e.code == 429:
                return "⚠️ [SYSTEM]: The Game Master is thinking too hard! (You hit the API rate limit. Please wait 60 seconds and try your action again.)"
            else:
                return f"⚠️ [SYSTEM]: A mystical anomaly occurred! (Error: {e})"
    def main_window(self):
        
        def enter_button_(*args):
            input = self.entry_bar.get()
            if not input.strip():
                return
            self.entry_bar.delete(0, "end")
            self.text_box.insert("end" , "\n\n\nYOU: "+input , "player_text")
            self.text_box.see("end")
            response = self.start(input)
            
            self.text_box.insert("end" , "\n\n\nAI: "+response , "ai_text")
            self.text_box.see("end")

        
        
        
        
        
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









system_prompt="""# SYSTEM INSTRUCTIONS

You are an expert Interactive Fiction Game Master.

Your job is to create and control a text-based adventure game.

You are NOT a chatbot, assistant, or tutor.

You only exist inside the game world.

Never mention AI, prompts, system rules, or internal logic.

Always stay in character.

The player is the main character of the story.

---

# CORE ROLE

You control:

* The world 🌍
* Events ⚡
* NPCs 🧍
* Enemies 👾
* Story flow 📖
* Consequences 🎭

The player controls:

* Actions
* Decisions
* Dialogue
* Problem solving
* Free-text responses

The world must react logically to everything the player does.

---

# STORY MEMORY

You must remember everything during the game:

* Player choices
* Inventory items
* Injuries and health
* Locations visited
* NPC interactions
* Clues and secrets
* Story events

Never contradict past events.

Never forget earlier story details.

---

# STORY STYLE

Write in **simple and easy English**.

Keep sentences clear and short.

Avoid difficult or poetic language.

Focus on:

* Clear action
* Easy understanding
* Strong atmosphere
* Fast storytelling

The player should always understand what is happening.

---

# ATMOSPHERE

Always describe the world clearly using:

* Weather 🌧️
* Sounds 🔊
* Smells 👃
* Light 🌙
* Environment 🌲
* Danger ⚠️

Use emojis naturally to improve visualization.

Do NOT spam emojis.

---

# INVENTORY & CONDITION

Do NOT show lists or stats.

Instead, include them naturally in the story.

Example:

* "You still hold a rusty key 🗝️ in your hand."
* "Your arm hurts after the last fight."
* "Your last healing potion 🧪 is almost gone."

---

# GAME FLOW RULE

Do NOT show:

❌ Objective
❌ Genre
❌ Danger level
❌ Turn numbers
❌ Chapters
❌ Progress bars

The story must feel continuous and natural.

---

# INTERACTION SYSTEM

The game uses TWO types of interaction:

## 1️⃣ Choice-Based Actions (about 60%)

You give 4 options.

Example:

What do you do?

1️⃣ Explore the cave
2️⃣ Walk deeper into the forest
3️⃣ Check your bag
4️⃣ Rest for a moment

💬 Or describe your own action.

---

## 2️⃣ Free-Text Interaction (about 40%)

Sometimes the player must type their own answer.

Use this for:

* Riddles 🧩
* Passwords 🔑
* Mystery clues 🕵️
* Dialogue responses 🐉
* Logic puzzles 🧠
* Story decisions ⚔️

Example:

A stone door blocks your way.

It says:

"I speak without a mouth and hear without ears."

💬 What is your answer?

---

# PLAYER CREATIVITY

Accept all reasonable answers.

Focus on meaning, not exact wording.

Reward creative thinking.

Allow multiple possible solutions when logical.

---

# CUSTOM ACTIONS

Player can type anything like:

💬 “I break the door with a rock”

You must decide if it is:

* Possible
* Dangerous
* Clever
* Risky

Then continue story logically.

---

# CONSEQUENCES

Every action matters.

Possible outcomes:

* Progress
* Injury
* Death
* Reward
* Loss of items
* New information
* Story changes

Dangerous choices can kill the player when appropriate.

---

# INVALID INPUT

If player input makes no sense:

❌ INVALID ACTION

Tell them briefly why.

Then repeat available choices or ask again.

Do not continue story until valid input is given.

---

# ENDINGS

## WIN

🎉🏆 YOU WIN 🏆🎉

Give a satisfying ending and close the story.

---

## LOSE / DEATH

☠️ GAME OVER ☠️

💀 You died

Explain what happened and end the story.

---

# RESPONSE FORMAT (VERY IMPORTANT)

Every reply must be ONLY:

📖 Story (simple, immersive, continuous)

Then:

⚡ What do you do?

1️⃣ Action
2️⃣ Action
3️⃣ Action
4️⃣ Action

💬 Or type your own action.

OR

🧩 If it is a puzzle:

Show the situation + ask question

💬 Your answer:

---

# IMPORTANT RULES

* No headings like “Turn 1”
* No stats panels
* No objectives shown
* No meta commentary
* No explanations outside story
* Keep everything immersive
* Always continue story based on player choice
* Always keep tension and consequences

"""

g = gui(system_prompt) 



















































































































































































from customtkinter import *
from tkcalendar import Calendar
import main
from CTkMessagebox import CTkMessagebox
from CTkTable import *





def button(width_ , height_ ,text_, pad_x_ ,pad_y_, master, **kwargs):
    button1=CTkButton(master= master, width=width_, height=height_, text=text_,  **kwargs)
    button1.place(relx= pad_x_ ,rely= pad_y_ ,anchor ="center")
    return button1



def label(width_ , height_ ,text_, pad_x_ ,pad_y_,  master , **kwargs):
    label=CTkLabel(master= master, text=text_, **kwargs)
    label.place(relx =pad_x_ ,rely=pad_y_ ,anchor ="center")
    return label


def entry(width_ , height_ ,text_, pad_x_ ,pad_y_,  master , **kwargs):
    entry=CTkEntry(master= master, width=width_, height=height_, placeholder_text=text_, **kwargs)
    entry.place(relx= pad_x_ ,rely= pad_y_ , anchor ="center")
    return entry


def drop_down_menu(width_ , height_ , pad_x_ ,pad_y_,   values  ,master , **kwargs):
    menu = CTkOptionMenu(master=master, width=width_, values=values ,height=height_, **kwargs)
    menu.place(relx=pad_x_, rely=pad_y_, anchor="center" )
    return menu

def radio_btn(width_ , height_ ,text_, pad_x_ ,pad_y_,  master , **kwargs):
    r_btn=CTkRadioButton(master= master, width=width_, height=height_, text=text_, **kwargs)
    r_btn.place(relx= pad_x_ ,rely= pad_y_ , anchor = "center")
    return r_btn

def tab(width_ , height_ , pad_x_ ,pad_y_,  master , **kwargs):
    tab=CTkTabview(master= master, width=width_, height=height_,  **kwargs)
    tab.place(relx= pad_x_ ,rely= pad_y_ ,anchor ="center")
    return tab


def scoll_pane(width_ , height_ , pad_x_ ,pad_y_,  master , **kwargs):
    sp=CTkScrollableFrame(master= master, width=width_, height=height_,**kwargs)
    sp.place(relx= pad_x_ ,rely= pad_y_ , anchor="center")
    return sp


def switch(width_ , height_ ,text_, pad_x_ ,pad_y_,  master , **kwargs):
    switch_=CTkSwitch(master= master, width=width_, height=height_, text=text_, **kwargs)
    switch_.place(relx =pad_x_,rely= pad_y_)
    return switch_
 
def textarea(width_ , height_ , pad_x_ ,pad_y_,  master , **kwargs):
    textarea_=CTkTextbox(master= master, width=width_, height=height_, **kwargs)
    textarea_.place(relx =pad_x_,rely= pad_y_ , anchor = "center")
    textarea_.configure(state ="normal")
    return textarea_

def segmented_button(width ,height, x , y , master ,values , **kwargs):
    s_btn=CTkSegmentedButton(master=master ,width=width ,height=height , values=values  , **kwargs)
    s_btn.place(relx = x , rely = y , anchor ="center")
    s_btn.set(values[0])
    return s_btn

def frame(width ,height, x , y , master  , **kwargs):
    frame_= CTkFrame(master= master ,width=width , height= height , corner_radius= 14 , **kwargs)
    frame_.place(relx= x ,rely = y , anchor = "center")
    return frame_


    

def add_income_expense_tab(tab_  , refresh_call = None):
    transaction_type= StringVar(value= "Expense")

    label(100 ,100 ,"Amount" , 0.15 ,0.2 ,tab_ ,font= CTkFont("Seoge UI", 25 ,"bold") )
    amount_entry = entry(200, 30,  "Enter Amount..." , 0.40, 0.2 , tab_)

    
    label(100 , 50, "Category" , 0.16 , 0.40 ,tab_ ,font=CTkFont("Seoge UI" ,25 ,"bold"))
    menu = drop_down_menu(150 ,35  ,0.4 ,0.40 , main.expense_categories ,tab_ )
    def update_category():
        if transaction_type.get() == "Income":
            menu.configure(values=main.income_categories)
            menu.set(main.income_categories[0])
        else:
            menu.configure(values=main.expense_categories)
            menu.set(main.expense_categories[0])

    radio_btn(100 ,100, "Income" ,0.7  ,0.2 ,tab_ , variable =transaction_type , value ="Income" ,font =CTkFont("Seoge UI", 18 ,"bold" ) , command = update_category)
    radio_btn(100 ,100, "Expense" ,0.87  ,0.2 ,tab_,variable =transaction_type , value ="Expense",font =CTkFont("Seoge UI", 18 ,"bold") , command = update_category )

    label(100 , 50, "Date" , 0.68 , 0.40 ,tab_ ,font=CTkFont("Seoge UI" ,25 ,"bold"))

    label(100 , 50, "Description" , 0.285 , 0.55 ,tab_ ,font=CTkFont("Seoge UI" ,20 ,"bold"))
    description_area = textarea(400 ,90 , 0.5 , 0.71 ,tab_)
    
    def datepicker(**kwargs):
        popup = CTkToplevel(tab_)
        popup.title("Choose Date")
        popup.geometry("240x260+350+225")
        popup.resizable(False, False)
        
        popup.attributes("-topmost", True)
        popup.grab_set() 
        
        cal = Calendar(popup, selectmode='day', date_pattern='y-mm-dd',background="darkblue", disabledbackground="black", bordercolor="black", headersbackground="black", normalbackground="black", foreground='white', normalforeground='white', headersforeground='white')
        cal.pack(pady=15, padx=15, fill="both", expand=True)
        def confirm_date():
            # Update the main window button text to show the selected date
            date_btn.configure(text=cal.get_date())
            popup.destroy() # Close the popup
            return cal.get_date()
        # Add a confirm button to the popup
        confirm_btn = CTkButton(popup, text="Confirm", command=confirm_date)
        confirm_btn.pack(pady=(0, 15))
    
    date_btn = button(130, 35 ,"Select a date" ,0.85 , 0.40, tab_ ,command = datepicker)

    def button_click():
        main_window = tab_.winfo_toplevel()
        try:
            amount = float(amount_entry.get())
            date = date_btn.cget("text")
            if date== "Select a date":
                CTkMessagebox(main_window, 200,200 ,"Error ⚠️" , "Please Select a Date.", icon="cancel")
            else:
                    

                type_ = transaction_type.get()
                category = menu.get()
                description = description_area.get("0.0","end").strip()
                
                amount_entry.delete(0 ,"end")
                menu.set(menu.cget("values")[0])
                date_btn.configure(text = "Select a date")
                description_area.delete("0.0","end")
                amount_entry.configure(text_color = ['gray14', 'gray84'])

                
                main.exp.add_expense_income(date,type_ ,amount ,category ,description)

                CTkMessagebox(main_window  ,250,250 ,"Success" , "Entry Added Successfully" ,icon="check")
                if refresh_call:
                    refresh_call()

        except ValueError:
            CTkMessagebox(main_window, 300,200 ,"Error ⚠️" , "Please enter a valid number for the amount.", icon="cancel")
            amount_entry.configure(text_color="red")


    button(150 ,40 , "Save !" ,0.5 , 0.93 , tab_ ,corner_radius = 15, command = button_click ,font=CTkFont("Seoge UI" ,25 ,"bold"))


def history_tab_(history_tab):
    label(100, 100, "History", 0.132, 0.1, history_tab, font=CTkFont("Arial", 30, "bold"))

    table_frame = scoll_pane(600, 290, 0.5, 0.57, history_tab)
    column_width = [85, 75, 85, 90, 235]

    # Mutable container so inner functions can reassign
    table_ref = [None]

    def build_table(filter_type="all"):
        # Destroy old table if it exists
        if table_ref[0] is not None:
            table_ref[0].destroy()

        if filter_type == "all":
            values = list(main.exp.list_incomes())
        elif filter_type == "income":
            values = list(main.exp.list_incomes("income"))
        else:
            values = list(main.exp.list_incomes("expense"))

        new_table = CTkTable(
            master=table_frame,
            values=values,
            colors=[("#F0F0F0", "#2C3542"), ("#E5E5E5", "#1A222B")],
            header_color="#0096FF",
            text_color=("black", "white")
        )
        for index, width in enumerate(column_width):
            new_table.edit_column(index, width=width)

        new_table.pack(expand=True, fill="both", padx=0, pady=0)
        table_ref[0] = new_table

    # Initial build
    build_table("all")

    def seg_btn_command(value):
        if value == "All":
            build_table("all")
        elif value == "Income":
            build_table("income")
        else:
            build_table("expense")

    sbtn = segmented_button(
        100, 20, 0.82, 0.1, history_tab,
        ["All", "Income", "Expenses"],
        command=seg_btn_command
    )

    def refresh():
        seg_btn_command(sbtn.get())

    return refresh


def dashboard_tab(master):

    CARD_THEMES = {
            "income": {
                "Dark":  {"fg": "#0D2318", "border": "#1a4a2e", "icon_bg": "#1a4a2e", "text": "#4ADE80", "sub": "#86EFAC", "icon": "↑"},
                "Light": {"fg": "#DCFCE7", "border": "#86EFAC", "icon_bg": "#BBF7D0", "text": "#166534", "sub": "#15803D", "icon": "↑"},
            },
            "expense": {
                "Dark":  {"fg": "#2A1010", "border": "#5a2020", "icon_bg": "#5a2020", "text": "#F87171", "sub": "#FCA5A5", "icon": "↓"},
                "Light": {"fg": "#FEE2E2", "border": "#FCA5A5", "icon_bg": "#FECACA", "text": "#991B1B", "sub": "#DC2626", "icon": "↓"},
            },
            "balance": {
                "Dark":  {"fg": "#0F1D30", "border": "#1e3a5f", "icon_bg": "#1e3a5f", "text": "#60A5FA", "sub": "#93C5FD", "icon": "◈"},
                "Light": {"fg": "#DBEAFE", "border": "#93C5FD", "icon_bg": "#BFDBFE", "text": "#1E3A5F", "sub": "#1D4ED8", "icon": "◈"},
            },
        }

    ic_light = CARD_THEMES["income"]["Light"]
    ic_dark = CARD_THEMES["income"]["Dark"]
    ec_light = CARD_THEMES["expense"]["Light"]
    ec_dark = CARD_THEMES["expense"]["Dark"]
    bc_light = CARD_THEMES["balance"]["Light"]
    bc_dark = CARD_THEMES["balance"]["Dark"]

    income ,expenses ,net = main.exp.summary()

    def dynamic_font(value):
        text = f"Rs. {value:,.0f}"
        if len(text) > 12:
            return CTkFont("Segoe UI", 14, "bold")
        elif len(text) > 9:
            return CTkFont("Segoe UI", 17, "bold")
        else:
            return CTkFont("Segoe UI", 22, "bold")

    income_card = frame(250 ,110 ,0.3 ,0.29 , master ,fg_color=(ic_light["fg"] , ic_dark["fg"]) , border_color=(ic_light["border"] ,ic_dark["border"]), border_width=2) 
    income_title = label(100 ,100 ,"TOTAL INCOME" ,0.5 ,0.22 ,master=income_card ,text_color=(ic_light["sub"] ,ic_dark["sub"] ) , font=CTkFont("Segoe UI", 10, "bold"))
    income_value = label(100 ,100 , f"Rs. {income:.1f}" ,0.5, 0.62 ,income_card ,text_color=(ic_light["text"], ic_dark["text"]) , font=dynamic_font(income))


    expense_card = frame(250 ,110 ,0.71 ,0.30 , master, fg_color=(ec_light["fg"] , ec_dark["fg"]) , border_color=(ec_light["border"] ,ec_dark["border"]), border_width=2)
    expense_title = label(100 ,100 ,"TOTAL EXPENSES" ,0.5 ,0.22 ,master=expense_card ,text_color=(ec_light["sub"] ,ec_dark["sub"] ) , font=CTkFont("Segoe UI", 10, "bold"))
    expense_value = label(100 ,100 , f"Rs. {expenses :.1f}" ,0.5, 0.62 ,expense_card , text_color=(ec_light["text"], ec_dark["text"]) ,  font=dynamic_font(expenses))


    balance_card = frame(520  ,110 ,0.5 , 0.68 , master ,fg_color=(bc_light["fg"] , bc_dark["fg"]) , border_color=(bc_light["border"] ,bc_dark["border"]), border_width=2 )
    balance_title = label(100 ,100 ,"NET BALANCE" ,0.5 ,0.22 ,master=balance_card ,text_color=(bc_light["sub"] ,bc_dark["sub"] ) , font=CTkFont("Segoe UI", 10, "bold"))
    balance_value = label(100 ,100 , f"Rs. {net:.1f}" ,0.5, 0.62 ,balance_card , text_color=(bc_light["text"], bc_dark["text"]) ,  font=CTkFont("Segoe UI", 22, "bold"))
 

    def refresh_dashboard():
        income ,expenses ,net = main.exp.summary()
        income_value.configure(text = f"Rs. {income:.1f}" ,font = dynamic_font(income))
        expense_value.configure(text = f"Rs. {expenses:.1f}" , font =dynamic_font(expenses))
        balance_value.configure(text = f"Rs. {net:.1f}")



    refresh_button = button(40 ,40, "↺" , 0.92 , 0.06 ,master ,  font = CTkFont("Seogi UI",30 ,"bold" ) , fg_color=(ic_light["fg"] , ic_dark["fg"]) , border_color=(ic_light["border"] ,ic_dark["border"]), border_width=2 , text_color=(ic_light["text"], ic_dark["text"]) ,command = refresh_dashboard)



def GUI_setup():
    set_appearance_mode("Dark")
    set_default_color_theme("dark-blue")

    app = CTk()
    app.resizable(width= False , height= False)
    app.minsize(800,600)
    app.title("Expense Tracker")


    label(100 ,100 ,"EXPENSE TRACKER", 0.5, 0.1, app, font = CTkFont("Arial", 40, "bold"))

    def mode_switch():
        if theme_switch.get():
            set_appearance_mode("Light")
            theme_switch.configure(text= "Dark Mode")
        else:
            set_appearance_mode("Dark")
            theme_switch.configure(text= "Light Mode")
    theme_switch = switch(20 ,20, "Light Mode", 0.85, 0.085 ,app, onvalue=1, offvalue=0, command = mode_switch)
    
    tab_=tab(700 , 450  , 0.5 ,0.55 , app, corner_radius=15)
    dashboard = tab_.add("Dashboard")
    income_expense_tab_ = tab_.add("Add Expense/Income")
    history_tab = tab_.add("History")
    tab_.set("Dashboard")

    refresh = history_tab_(history_tab)
    add_income_expense_tab(income_expense_tab_  , refresh)
    dashboard_tab(dashboard)

    app.mainloop()
    
GUI_setup()
    




    
    
        

















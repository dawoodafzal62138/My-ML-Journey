from customtkinter import *





def button_click():
    set_appearance_mode("light")

def button(width_ , height_ ,text_, pad_x_ ,pad_y_, master, **kwargs):
    button1=CTkButton(master= master, width=width_, height=height_, text=text_,  **kwargs)
    button1.place(x= pad_x_ ,y= pad_y_)



def label(width_ , height_ ,text_, pad_x_ ,pad_y_,  master , **kwargs):
    label=CTkLabel(master= master, width=width_, height=height_, text=text_, **kwargs)
    label.place(relx =pad_x_ ,rely=pad_y_ ,anchor ="center")
    return label


def entry(width_ , height_ ,text_, pad_x_ ,pad_y_,  master , **kwargs):
    entry=CTkEntry(master= master, width=width_, height=height_, placeholder_text=text_, **kwargs)
    entry.place(relx= pad_x_ ,rely= pad_y_ , anchor ="center")

def frame(width_ , height_ ,text_, pad_x_ ,pad_y_,  master , **kwargs):
    frame=CTkFrame(master= master, width=width_, height=height_, text=text_, **kwargs)
    frame.place(x= pad_x_ ,y= pad_y_)


def drop_down_menu(width_ , height_ , pad_x_ ,pad_y_,   values  ,master , **kwargs):
    menu = CTkOptionMenu(master=master, width=width_, values=values ,height=height_, **kwargs)
    menu.place(relx=pad_x_, rely=pad_y_, anchor="center" )
    return menu

def radio_btn(width_ , height_ ,text_, pad_x_ ,pad_y_,  master , **kwargs):
    r_btn=CTkRadioButton(master= master, width=width_, height=height_, text=text_, **kwargs)
    r_btn.place(relx= pad_x_ ,rely= pad_y_ , anchor = "center")


def tab(width_ , height_ , pad_x_ ,pad_y_,  master , **kwargs):
    tab=CTkTabview(master= master, width=width_, height=height_,  **kwargs)
    tab.place(relx= pad_x_ ,rely= pad_y_ ,anchor ="center")
    return tab


def scoll_pane(width_ , height_ ,text_, pad_x_ ,pad_y_,  master , **kwargs):
    sp=CTkScrollableFrame(master= master, width=width_, height=height_, text=text_, **kwargs)
    sp.place(x= pad_x_ ,y= pad_y_)


def switch(width_ , height_ ,text_, pad_x_ ,pad_y_,  master , **kwargs):
    switch_=CTkSwitch(master= master, width=width_, height=height_, text=text_, **kwargs)
    switch_.place(relx =pad_x_,rely= pad_y_)
    return switch_




def add_income_expense_tab(tab_):
    transaction_type= StringVar(value= "Expense")


    label(100 ,100 ,"Amount" , 0.15 ,0.2 ,tab_ ,font= CTkFont("Seoge UI", 25 ,"bold") )
    entry(200, 30,  "Enter Amount..." , 0.40, 0.2 , tab_)
    r1= radio_btn(100 ,100, "Income" ,0.7  ,0.2 ,tab_ , variable =transaction_type , value ="Income" ,font =CTkFont("Seoge UI", 18 ,"bold"))
    radio_btn(100 ,100, "Expense" ,0.90  ,0.2 ,tab_,variable =transaction_type , value ="Expense",font =CTkFont("Seoge UI", 18 ,"bold") )
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
    # if 
    label(100 ,100 ,"Category" , 0.15 ,0.2 ,tab_ ,font= CTkFont("Seoge UI", 25 ,"bold") )
    drop_down_menu(100 ,30  ,0.15 ,0.5 , income_categories ,tab_ )



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
    tab_.add("Dashboard")
    income_expense_tab_ = tab_.add("Add Expense/Income")
    tab_.add("History")
    tab_.set("Dashboard")

    add_income_expense_tab(income_expense_tab_)
        




    app.mainloop()





GUI_setup()








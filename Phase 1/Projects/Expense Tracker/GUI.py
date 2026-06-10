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
    label=CTkLabel(master= master, width=width_, height=height_, text=text_, **kwargs)
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



    

def add_income_expense_tab(tab_ ):
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

        except ValueError:
            CTkMessagebox(main_window, 300,200 ,"Error ⚠️" , "Please enter a valid number for the amount.", icon="cancel")
            amount_entry.configure(text_color="red")


    button(150 ,40 , "Save !" ,0.5 , 0.93 , tab_ ,corner_radius = 15, command = button_click ,font=CTkFont("Seoge UI" ,25 ,"bold"))


def history_tab_(history_tab):
    label(100 ,100 ,"History", 0.132, 0.1, history_tab, font = CTkFont("Arial", 30, "bold"))
    tables_value = list(main.exp.list_incomes()) 
    def seg_btn_command(value):
        global tables_value
        if value == "All" :
            tables_value = list(main.exp.list_incomes()) 
        elif value == "Income": 
            tables_value = list(main.exp.list_incomes("income")) 
        else: 
            tables_value = list(main.exp.list_incomes("expense")) 

        history_table.update_values(values=tables_value)



    segmented_button(100 ,20, 0.82 ,0.1 , history_tab ,["All","Income" ,"Expenses"] , command = seg_btn_command)




    table_frame=scoll_pane(600 ,290 , 0.5 ,0.57 ,history_tab )
    column_width= [85, 75, 85, 90, 235]
    history_table = CTkTable(master=table_frame, values= tables_value, colors=[("#F0F0F0", "#2C3542"), ("#E5E5E5", "#1A222B")],header_color="#0096FF",text_color=("black", "white"),command=seg_btn_command)
    for index , width  in enumerate(column_width):
        history_table.edit_column(index , width = width)
    
    history_table.pack(expand=True, fill="both", padx=0, pady=0)


  

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
    history_tab=tab_.add("History")
    tab_.set("History")

    add_income_expense_tab(income_expense_tab_ )
    history_tab_(history_tab)
        




    app.mainloop()





GUI_setup()








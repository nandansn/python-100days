from curses import window
import tkinter as tk
from tkinter import ttk
from turtle import bgcolor


def calculate_interest(ir_entry, amt_entry, months_entry):
    def calc():
        int_per_month = ((float(ir_entry.get()) * float(amt_entry.get()))/ 1200) 
        
        total = int_per_month * float(months_entry.get())

           # per_month_label_entry
        per_month_label = ttk.Label(text="Per Month :", width=20, justify='center', font=('Verdana',18))
        per_month_label.grid(row=3,column=0,padx=30,pady=10)

        per_month_vlabel = ttk.Label(text="{}".format(int(int_per_month)), width=10, anchor='center', font=('Verdana',18))
        per_month_vlabel.grid(row=3,column=1,padx=30,pady=10)

        # per_month_label_entry
        total_label = ttk.Label(text="For {} months:".format(months_entry.get()), width=20, anchor='w', font=('Verdana',18))
        total_label.grid(row=4,column=0,padx=30,pady=10)

        total = ttk.Label(text="{}".format(int(total)), width=20, anchor='center', font=('Verdana',18))
        total.grid(row=4,column=1,padx=30,pady=10)
    return calc




def create_main_window():
    window = tk.Tk()
    window.title("Finance Calculator")
    window.geometry("800x300")

     # amt_label_entry
    amt_label = ttk.Label(text="Amount :", width=20, justify='center', font=('Verdana',18))
    amt_label.grid(row=0,column=0,padx=30,pady=30)

    amt_entry = ttk.Entry(width=30, justify='center', font=('Verdana',18))
    amt_entry.grid(row=0,column=1,padx=30,pady=30)
    
    
    # interest_rate_label_entry
    ir_label = ttk.Label(text="Interest Rate :", width=20, justify='center', font=('Verdana',18))
    ir_label.grid(row=1,column=0,padx=30,pady=10)

    ir_entry = ttk.Entry(width=10, justify='center', font=('Verdana',18))
    ir_entry.grid(row=1,column=1,padx=30,pady=10)

     # months_label_entry
    months_label = ttk.Label(text="Months :", width=20, justify='center', font=('Verdana',18))
    months_label.grid(row=2,column=0,padx=30,pady=10)

    months_entry = ttk.Entry(width=10, justify='center', font=('Verdana',18))
    months_entry.grid(row=2,column=1,padx=30,pady=10)

   

   

    


    calc_button = ttk.Button(text="Calculate", width=20, command=calculate_interest(ir_entry, amt_entry, months_entry))
    calc_button.grid(row=5,column=1,padx=30,pady=20)

     
    

    window.mainloop()


create_main_window()
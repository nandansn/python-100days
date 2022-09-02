import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.minsize(500,500)

#create label
my_label = tk.Label(text="New Label",font=('verdana',24))
#display
my_label.pack()


def change_color():
    my_label.config(text="changed")


# text box
name_text = ttk.Entry()
name_text.pack()

def create_user_label():
    input = name_text.get()
    ttk.Label(text=input).pack()
    


#create button
my_btn = ttk.Button(text="change_label", command=change_color)
my_btn.pack()

ttk.Button(text="Create Label",command=create_user_label).pack()

window.mainloop()
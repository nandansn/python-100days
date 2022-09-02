from cgitb import text
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.minsize(500,500)
window.title("Unit Converter")
window.config(padx=20,pady=20)

mile_label = tk.Label(text=" Mile: ")
mile_label.grid(row=0,column=0,padx=10,pady=10)

mile_entry = tk.Entry()
mile_entry.config(width=10,text=0)
mile_entry.grid(row=0,column=1)

km_label = tk.Label(text="0")
km_label.grid(row=2,column=1)

def mile_to_km(m):
    def convert():
        c = int(m.get()) * 1.61
        km_label.config(text=c)
    return convert



btn = ttk.Button(text="Click to Convert", command=mile_to_km(mile_entry))
btn.grid(row=1,column=1)




window.mainloop()


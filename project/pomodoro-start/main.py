
from tkinter import Canvas, PhotoImage, Tk
from tk import *




# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.geometry('600x600')
window.config(background=YELLOW)




canvas = Canvas(width=400,height=400)

img = PhotoImage(name='./tomato.gif')
#canvas.create_image(100,100,image=img)



canvas.pack()

window.mainloop()



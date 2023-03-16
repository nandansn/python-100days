from cgitb import text
import tkinter 

window = tkinter.Tk()
window.title("Hello world!!")
window.minsize(width=500, height=500)

label = tkinter.Label(text="Hello",font=('Arial', 30))
label.pack()


window.mainloop()

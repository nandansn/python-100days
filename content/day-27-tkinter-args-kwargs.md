## Tkinter
- python module to create gui
- in any gui, the parent component is window
- in the parent component we add other gui components like label, button, textbox etc

### How to create a window?
- in the tkinter module, create object for Tk()
- call mainloop() method display the window continously

> import tkinter 
>
> window = tkinter.Tk()
> window.mainloop()

### how to add a component in the window?

- initialize the component
- display the component using pack method

- for example to add lable, you need to initalize label component
- after that you need to set the label text, you can mention size, style
- then you need to add in the window


### buttons, label, entry
- button, use command argument to pass the function, which will be executed on click
- entry, used to get the input from the user, textbox. get() method is called to get the value


### other tkninter widgets
- Text, text box. we can enter multiline text. we can specify the width, height, number of rows cols,
- focus() method to focus on any widget component
- Spinbox(), 
- Scale()
- Checkbox(), for on / off
- Radiobutton(), only one is selected
- Listbox(), to select list of values, we can use bind() to bind the action and the list item, use insert() method to add an item


### Layout managers
- pack() - postion the widgets from the starting position, default it places at the top, you can specify the position by **side** argument [left,tight,top,bottom]
- place() - position the widgets using the x,y coordinates place(10,50)
- grid() - position the widget using the grid(), you can pass the column and row
-  you can use padx and pady to add space around the component






### optional arguments

- when defining the function, you can mention the option argument in the function
- these optional args are used when you don't pass the value in the function
- Spinbox, component used for incrementer with from, to configuration

### many positional arguments
- defining fucntion with many positional arguments *args, this is tuple
- you can pass any number of arguments to the function


## keyword arguments
- defining the function with keyword arguments, **kwargs, this is dict
- we can pass the zero or more arguments
- args will be key value pair, will be usefuk hen intializing the object with optional attributes


### tkinter ref

[ref] (https://www.pythontutorial.net/tkinter/tkinter-pack/)
from tkinter import *
from tkinter import messagebox

def convert():
    try:
        val = float(value_entry.get()) 
    except:
        messagebox.showinfo('Error!','Please enter a number!')
        val = 0
        
    result = val * 0.621371
    entryVal.set(result)

def copyr():
    messagebox.showinfo("","Dr Grey, 2016")

def helpWin():
    win = Tk()
    win.title("Help")
    help1 = Label (win,text = "Km to miles converter") 
    help1.pack()
    win.mainloop()

# Set up window
window = Tk()
# Title appears in bar
window.title("Distance converter")
# Specify the dimensions of the window in pixels
window.geometry("300x100")

entryVal    = StringVar() 

# Add widgets
title_label    = Label(window,text='Convert from km to miles')
entry_label    = Label(window, text='Enter distance in km')
value_entry    = Entry(window)
result_label   = Label(window,text='Distance in miles')
#entryVal.set(value_entry.get())
result_entry   = Label(window, textvariable=entryVal)
convert_button = Button(window, text='Convert',command=convert)

#####
menuBar = Menu(window)
fileMenu = Menu(menuBar, tearoff=0)
helpMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=fileMenu)     
menuBar.add_cascade(label="Help", menu=helpMenu)
fileMenu.add_command(label="Run",command=convert)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=window.destroy)
helpMenu.add_command(label="Help", command=helpWin)
helpMenu.add_command(label="About", command=copyr) 
window.config(menu=menuBar)

# Pack labels into window
title_label.grid(column=0, row=0, columnspan=2,sticky=(W,E))    
entry_label.grid(column=0, row=1,sticky=(W))
value_entry.grid(column=1, row=1,sticky=(W))
result_label.grid(column=0, row=2,sticky=(W))
result_entry.grid(column=1, row=2,sticky=(W))   
convert_button.grid(column=0, row=3,sticky=(W,E)) 

window.mainloop()


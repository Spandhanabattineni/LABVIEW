import tkinter
from tkinter import *
from tkinter import Button

win= Tk()
win.geometry("800x300")
menu =StringVar()

menu.set("Select Device")
drop= OptionMenu(win, menu, "Device A", "Device B", "UBD5")
drop.pack()
button: Button = tkinter.Button(win, text='RUN', width=40)
button.pack()
win.mainloop()
print('Successful')
from tkinter import *
import customtkinter
import tkinter as tk 
from tkinter import ttk



root = Tk()
root.geometry('500x500')

s = ttk.Style()
s.configure('mainframe.TFrame', background='black')

mainframe = ttk.Frame(root, width=50, height=500, style='mainframe.TFrame')
mainframe.grid(row=0, column=0)
# mainframe.grid(row=0, column=3, rowspan=1, columnspan=1, sticky=W)


# fram2 = Frame(root, width=200, height=200)
# fram2.grid(row=1, column=0, sticky='WENS')
# fram2.config(bg='#579BB1')


# fram3 = Frame(root, width=250, height=250)
# fram3.grid(row=0, column=1, sticky='snwe')
# fram2.config(bg='teal')


# fram4 = Frame(root, width=250, height=250)
# fram4.grid(row=1, column=1, sticky='NSEW')
# fram4.config(bg='red')


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.columnconfigure(2, weight=3)
root.rowconfigure(1, weight=2)
root.rowconfigure(2, weight=2)




# root.resizable(width=1, height=1)
root.mainloop()
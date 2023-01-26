import os
from tkinter import *
import customtkinter


customtkinter.set_appearance_mode('dark')
"""window.geometry(1366x768)"""

root = customtkinter.CTk()
root.geometry('800x500+300+130')
root.title('Home Page')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=0)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=0)



label = customtkinter.CTkLabel(master=root, text='Welcome to DS Enterprice', font=('Times', 40))
label.grid()




root.mainloop()
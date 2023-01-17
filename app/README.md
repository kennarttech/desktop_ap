# 
creating new modern gui using customtkinter

 # 
Adding new color style to the window or frame invole 

1. import tkinter as tk
2. from tkinter import ttk

my_style = ttk.Style()
my_style.configure('mainframe.TFrame', background='black')



# ...uses:!!
subframe = ttk.Frame(root, width=2, height=2, style='mainframe.TFrame')
subframe.grid()


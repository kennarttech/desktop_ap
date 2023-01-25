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




# s = ttk.Style()
frame.grid_columnconfigure(0, weight=1, minsize=100, pad=5)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=2)
frame.grid_columnconfigure(2, weight=3)
frame.grid_columnconfigure(0,3,weight=1)


#
1. Whether grid_columnconfigure or columnconfigure is the best method to use depends on the specific use case and requirements of the project.

2. columnconfigure is generally used to configure the columns of the root window, which can be useful when you want to configure the columns of the entire window. This can be useful when you want to set a global layout for the entire window, such as having the same weight or minimum size for all columns.

3. On the other hand, grid_columnconfigure is generally used to configure the columns of a specific parent widget, such as a frame. This can be useful when you want to set a specific layout for a specific part of the window, such as having different weights or minimum sizes for different columns within a frame. Additionally grid_columnconfigure provides more options, which allows for more flexibility in the layout.

4. In general, it is best to use the method that best suits the specific requirements of the project and provides the most flexibility and control over the layout.
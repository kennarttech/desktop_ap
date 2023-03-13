"""This are built-in modules, which are part of the Python Standard Library"""
import os
import json
import tkinter as tk
from tkinter import ttk
from tkinter import NSEW
from tkinter import PhotoImage


"""this are third-party modules that need to be installed separately using pip"""
import customtkinter
from PIL import Image
from CTkMessagebox import CTkMessagebox


class ResultTable(customtkinter.CTkFrame):
    def __init__(self, master, width: int=1000, 
                 height: int=600) -> None:
        super().__init__(master)
        self.master_window = master
        self.width = width
        self.height = height
        self.anything = True 


        self.master_window.geometry(f'{width}x{height}+155+50')
        self.style = ttk.Style(master=self.master_window)
        self.style.theme_use('clam')


        self.style.configure('Treeview', background="gray28",
                             foreground='white', rowheight=60,
                             fieldbackground="#292929")
        

        self.style.map('Treeview', 
                       background=[('selected', '#347083')])


        customtkinter.set_appearance_mode('system')
        customtkinter.set_default_color_theme('green')


        self.icon_image = PhotoImage(file='app/icons/logo_03.png')
        self.master_window.tk.call('wm', 'iconphoto', self.master_window._w, 
                                   self.icon_image)
        

        self.master_window.columnconfigure(0, weight=1, uniform='a')
        self.master_window.rowconfigure(1, weight=1, uniform='a')


        self.top_frame = customtkinter.CTkFrame(master=self.master_window, 
                                                fg_color='#2C3333', 
                                                height=45, corner_radius=2,
                                                bg_color='#2C3333')
        self.top_frame.grid(row=0, column=0, pady=(0, 0), ipady=3, sticky='nsew')
        self.top_frame.grid_columnconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')


        self.top_frame_label = customtkinter.CTkLabel(master=self.top_frame, 
                                                      text='View Data', 
                                                      font=('Roboto', 22),
                                                      text_color='white')
        self.top_frame_label.grid(row=0, column=2, padx=(1, 1), pady=(10, 1), 
                                  sticky=NSEW)


        self.middle_frame = customtkinter.CTkFrame(master=self.master_window, 
                                                   fg_color='#20262E',)
        self.middle_frame.grid(row=1, column=0, rowspan=4, pady=(1, 1), 
                               sticky=NSEW)


        self.tree = ttk.Treeview(master=self.middle_frame, 
                                 columns=("col1", "col2", "col3"), 
                                 show='headings')
        

        self.tree['columns'] = ('one', 'two', 'three')
        self.tree.heading("one", text='Column 1')
        self.tree.heading("two", text='Column 2')
        self.tree.heading("three", text='Column 3')
        self.tree.column("one", width=400)
        self.tree.column("two", width=400)
        self.tree.column("three", width=400)


        for i in range(100):
            self.tree.insert("", tk.END, 
                             values=(f'Value {i}', f'Value {i*2}', f"Value {i*3}"))
            

        self.vsb = customtkinter.CTkScrollbar(master=self.middle_frame,
                                            #   button_hover_color='#FF0303', 
                                              orientation='vertical', 
                                              command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side='right', fill='y')


        self.hsb = customtkinter.CTkScrollbar(master=self.middle_frame,
                                            #   button_hover_color='#FF0303', 
                                              orientation='horizontal', 
                                              command=self.tree.xview)
        self.tree.configure(xscrollcommand=self.hsb.set)
        self.hsb.pack(side='bottom', fill='x')

        self.tree.pack(expand=True, fill='both')


        # self.footer_frame = customtkinter.CTkFrame(master=self.master_window,
        #                                            fg_color='#2C3333', height=30)
        # self.footer_frame.grid(row=2, column=0, pady=(0, 0), sticky=NSEW)

        # self.master_window.mainloop()



if __name__ == "__main__":
    # result__tb = customtkinter.CTk()
    result__tb = customtkinter.CTkToplevel()
    result__tb.minsize(920, 530)
    result__tb.title('Result Table')
    result__tb.attributes('-zoomed', True)
    app = ResultTable(result__tb)

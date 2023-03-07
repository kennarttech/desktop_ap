"""This are built-in modules, which are part of the Python standard Library"""
import os
import sys
import json
from tkinter import * 
from tkinter import messagebox


"""This are third-party modules that need to be installed separately using pip"""
import customtkinter
from PIL import Image


"""This are local modules that i have created myself and are part of the project"""
from custommessage import Closewindowdhboard


class BaseCustomNote(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master


        customtkinter.set_appearance_mode('system')
        customtkinter.set_default_color_theme('green')


        self.topframe = customtkinter.CTkFrame(self, width=700, height=40,
                                               corner_radius=15, border_width=4)
        self.topframe.grid(row=0, column=0)
        self.topframe.grid_columnconfigure((2), weight=1, uniform='a')
        self.topframe.grid_rowconfigure((1), weight=1, uniform='a')

        self.grid(row=0, column=0, pady=70, rowspan=2, columnspan=4)


class CustomNote(BaseCustomNote):
    def __init__(self, master):
        super().__init__(master)

        default = customtkinter.set_default_color_theme('green')


        self.notetitle = customtkinter.CTkEntry(self.topframe, width=400, 
                                                height=35, font=(('Sans'), 16),
                                                placeholder_text='Note title',
                                                corner_radius=15)
        self.notetitle.grid(row=0, column=0, padx=(0,40), pady=(5, 0))
        # self.notetitle.focus()


        self.textbox = customtkinter.CTkTextbox(self.topframe, width=600, 
                                               height=400, corner_radius=10,
                                               border_width=1, font=(('Sans'), 17),
                                               scrollbar_button_hover_color='#16FF00')
        self.textbox.grid(row=1, column=0, padx=(15, 22), pady=(20, 15))
        self.textbox.insert(0.0, 'Please enter your note here')
        self.textbox.focus()


        self.button = customtkinter.CTkButton(self.topframe, text='Close',
                                              fg_color=default, height=28,
                                              corner_radius=8, command=self.syclos)
        self.button.grid(row=1, column=1, padx=(0, 15), pady=(0, 120))


        self.button = customtkinter.CTkButton(self.topframe, text='Save',
                                              fg_color=default, height=28,
                                              corner_radius=8)
        self.button.grid(row=1, column=1, padx=(0, 15), pady=(10, 10))


    def syclos(self):
        # Closewindowdhboard(self.topframe)
        if messagebox.askyesno('Close Notebook', 
                               'Save your data before closing\n'
                               "Do you want to close the notepad",icon='info'):
            self.destroy()
        else:
            return self.master








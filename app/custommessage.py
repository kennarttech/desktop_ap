"""This are built-in modules, which are part of the Python Standard Library"""
import os
import sys
import json
from tkinter import *


"""this are third-party modules that need to be installed separately using pip"""
import customtkinter 
from PIL import Image


class Message(customtkinter.CTkFrame):
    """This class defines the Popupmessage, that is use create the GUI"""


    """Using contex manager to load json file"""
    with open(file='app/config/settings.json', mode='r', encoding='utf-8') as rf:
        user_message = json.load(rf)


    def __init__(self, master) -> None:
        super().__init__(master)
        self.master = master


        customtkinter.set_appearance_mode('brown')
        customtkinter.set_default_color_theme('green')


        self.message = customtkinter.CTkFrame(self, border_width=2, 
                                              fg_color='gray31',
                                              bg_color='gray25',
                                              border_color='gray40',
                                              corner_radius=15)
        self.message.grid(row=0, columnspan=2)
        self.message.grid_columnconfigure(2)


        self.yes_button = customtkinter.CTkButton(self.message, text='Yes', 
                                                  width=100, command=self.close)
        self.yes_button.grid(row=1, column=1, pady=10, padx=20)


        self.no_button = customtkinter.CTkButton(self.message, text='No', 
                                                 width=100, command=self.destroy)
        self.no_button.grid(row=1, column=0, pady=10, padx=20)


        self.grid(row=0, column=0, rowspan=3, columnspan=3)


    def close(self):
        self.destroy()
        self.master.destroy()
        sys.exit()


class Closewindowdhboard(Message):
    """This class inherit from Message class (base class), which is use to msg popup"""


    def __init__(self, master) -> str:
        super().__init__(master)


        self.image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 
                                       "icons")
        self.message_icon = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, 
                                                    "logo_02.png")), 
        size=(50, 50))


        self.main_label = customtkinter.CTkLabel(self.message, width=200,
                                                 text=self.user_message['usermessage'],
                                                 image=self.message_icon, 
                                                 text_color=self.user_message['message_text_color'],
                                                 compound='left', font=('Sans', 15))
        self.main_label.grid(row=0, column=0, columnspan=2, padx=(20, 20), pady=20)






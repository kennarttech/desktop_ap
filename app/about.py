"""This are built-in modules, which are part of the Python Standard Library"""
import json
import tkinter as tk
from tkinter import *


"""this are third-party modules that need to be installed separately using pip"""
import customtkinter


"""The are local modules that I have created myself and are part of the project. """
import homepage


class Aboutpage(customtkinter.CTkToplevel):
    """This class defines the aboutpage, that is use create the GUI"""
    customtkinter.set_appearance_mode('system')


    """Using contex manager to open txt file for reading mode"""
    TEXT_FILE_PATH = "app/config/about.json"

    with open(file=TEXT_FILE_PATH, mode='r', encoding='utf-8') as rf:
        app_about = json.load(rf)


    def __init__(self) -> None:
        # self.about = customtkinter.CTk()
        self.about = customtkinter.CTkToplevel()
        self.about.title('About Page')
        self.about.geometry('620x450+360+120')
        icon_image = PhotoImage(file='app/icons/logo_04.png')
        self.about.tk.call('wm', 'iconphoto', self.about._w, icon_image)
      

        self.about.columnconfigure(0, weight = 1, uniform='a')
        self.about.columnconfigure(1, weight = 0)
        self.about.rowconfigure(1, weight = 1)


        top_frame = customtkinter.CTkFrame(self.about, 
                                            border_width = 0.6, 
                                            border_color ='gray10',
                                            corner_radius = 3,)
        top_frame.grid(row = 0, column = 0, ipady=3, sticky = NSEW)
        top_frame.grid_columnconfigure(0, weight = 1)


        home_button1 = customtkinter.CTkButton(top_frame, text='Exit', 
                                                height=20, fg_color="transparent", 
                                                font=('Roboto', 13), width=50, 
                                                hover_color=("gray70", "gray30"), 
                                                corner_radius=5, command=self.aboutexit,
                                                text_color=("gray10", "gray90"),
                                                border_color='gray40',border_width=1)
        home_button1.grid(row=2, column=0, padx=(20, 10), pady=(7, 0), sticky=N)


        default_textbox = customtkinter.CTkTextbox(self.about, width=200, font=('Times', 20),
                                                    text_color=('gray80'), corner_radius=10,
                                                    scrollbar_button_hover_color=('#16FF00'))
        default_textbox.grid(row=1, column=0, padx=(30, 30), pady=(30, 40), sticky="nsew")
        default_textbox.insert(0.0, 'About the application\n*------------------------*'+ '\n\n' + 
                               self.app_about['app_description']['appname'])
        default_textbox.configure(state='disable')


        footer_frame = customtkinter.CTkFrame(self.about, border_width = 0.6, 
                                            border_color ='gray10',
                                            fg_color='gray25', 
                                            corner_radius = 3,)
        footer_frame.grid(row = 2, column = 0, ipady=1, sticky=EW)
        footer_frame.grid_columnconfigure((0,1,2), weight = 1)


        footer_text = customtkinter.CTkLabel(footer_frame, 
                                            text=self.app_about['statusbar']['KT'],
                                            font=customtkinter.CTkFont('Sans', 12),)
        footer_text.grid(row=0, column=1, pady=2)


        # self.about.mainloop()


    """This method exit the about window when the button is press"""
    def aboutexit(self) -> None:
        homepage.Homepage(self.about)
        self.about.destroy()



if __name__ == "__main__":
    """this returns True if the script is run directly else it return False"""
    app = Aboutpage()
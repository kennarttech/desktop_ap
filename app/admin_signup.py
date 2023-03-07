"""This are built-in modules, which are part of the Python Standard Library"""
import os
from tkinter import *


"""this are third-party modules that need to be installed separately using pip"""
import customtkinter
from PIL import Image


"""The are local modules that I have created myself and are part of the project. """
import login


class Adminignup(customtkinter.CTkToplevel):
    """This class defines the Adminsignup page, which is use create the GUI"""


    def __init__(self):
        # self.register = customtkinter.CTk()
        self.register = customtkinter.CTkToplevel()
        self.register.title('[Signup]')
        self.register.resizable(0, 0)
        self.register.geometry('500x500+400+100')
        icon_image_ = PhotoImage(file='app/icons/logo_02.png')
        self.register.tk.call('wm', 'iconphoto', self.register._w, icon_image_)


        self.register.columnconfigure(0, weight=1, uniform='a')
        self.register.rowconfigure(1, weight=0, uniform='a')


        image_path = os.path.join(os.path.dirname(os.path.relpath(__file__)), 
                                                'icons')
        logimage = customtkinter.CTkImage(Image.open(os.path.join(image_path, 
                                        'Google__G__Logo.svg.webp')),
        size=(17, 17))


        self.background_image = PhotoImage(file='app/icons/pattern.png')
        self.background_label = Label(self.register, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)


        frame = customtkinter.CTkFrame(self.register, width=320, height=400, 
                                        corner_radius=10, 
                                        border_color='gray50')
        frame.pack(pady=60, anchor='center')
        frame.grid_columnconfigure((0,1,2), weight=0)
        frame.grid_rowconfigure((0,1,2), weight=1)


        title_lable = customtkinter.CTkLabel(frame, text='Signup.',
                                            font=customtkinter.CTkFont('Sans', 20))
        title_lable.place(x=130, y=30)

        
        user_name = customtkinter.CTkEntry(frame, width=220, height=32,
                                            placeholder_text='Enter your username',
                                            font=('Sans', 14))
        user_name.place(x=53, y=70)
        user_name.focus()


        user_password = customtkinter.CTkEntry(frame, width=220, height=32,
                                            placeholder_text='Enter your password', 
                                            show='....', font=('Sans', 14))
        user_password.place(x=53, y=130)


        comfirm_password = customtkinter.CTkEntry(frame, width=220, height=32,
                                            placeholder_text='Comfirm password', 
                                            show='....', font=('Sans', 14))
        comfirm_password.place(x=53, y=190)


        register_btn = customtkinter.CTkButton(frame, text='register', width=220, 
                                                height=32,corner_radius=5,
                                                font=customtkinter.CTkFont('Sans', 13),
                                                hover_color=('#3CCF4E'),
                                                fg_color='transparent',
                                                border_color='gray40',
                                                border_width=0.6)
        register_btn.place(x=54, y=245)


        forgot_password = customtkinter.CTkButton(frame, fg_color='transparent',
                                                text='Already have account? Login.', 
                                                height=20, width=100, corner_radius=5,
                                                font=customtkinter.CTkFont('Sans', 13),
                                                hover_color=('gray70', 'gray30'),
                                                border_color='gray40',
                                                command=self.login_function)
        forgot_password.place(x=65, y=285)


        alternative_btn = customtkinter.CTkButton(frame, border_color='gray40',
                                                text='Register using google', width=220, 
                                                height=30,corner_radius=5, image=logimage,
                                                font=customtkinter.CTkFont('Sans', 13),
                                                hover_color=('#3CCF4E'), compound='left',
                                                fg_color=('gray7', 'gray30'),
                                                border_width=0.6
                                                )
        alternative_btn.place(x=54, y=320)

        # self.register.mainloop()


    def login_function(self)-> None:
        login.LoginUser()
        self.register.destroy()





if __name__ == "__main__":
    app = Adminignup()

"""This are built-in modules, which are part of the Python Standard Library"""
import os
from tkinter import *


"""this are third-party modules that need to be installed separately using pip"""
import customtkinter
from PIL import Image
from CTkMessagebox import CTkMessagebox


"""The are local modules that I have created myself and are part of the project."""
import register 
import dashboard
import forget_password


class LoginUser(customtkinter.CTkToplevel):
    def __init__(self):
        # self.login = customtkinter.CTk()
        self.login = customtkinter.CTkToplevel()
        self.login.title('[Login]')
        self.login.resizable(0, 0)
        self.login.geometry('500x500+400+100')
        icon_image_ = PhotoImage(file='app/icons/logo_02.png')
        self.login.tk.call('wm', 'iconphoto', self.login._w, icon_image_)


        self.login.columnconfigure(0, weight=1, uniform='a')
        self.login.rowconfigure(1, weight=0, uniform='a')


        image_path = os.path.join(os.path.dirname(os.path.relpath(__file__)), 
                                                                'icons')
        logimage = customtkinter.CTkImage(Image.open(os.path.join(image_path,
                                                    'Google__G__Logo.svg.webp')),
        size=(17, 17))


        self.background_image = PhotoImage(file='app/icons/pattern.png')
        self.background_label = Label(self.login, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)


        frame = customtkinter.CTkFrame(self.login, width=320, height=400, 
                                        corner_radius=10, 
                                        border_color='gray50')
        frame.pack(pady=60, anchor='center')
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure((0,1,2), weight=1)


        title_lable = customtkinter.CTkLabel(frame, text='Login into your account',
                                            font=customtkinter.CTkFont('Sans', 20))
        title_lable.place(x=45, y=30)
        

        self.user_name = customtkinter.CTkEntry(frame, width=220, height=32,
                                            placeholder_text='Enter your username',
                                            font=('Sans', 14))
        self.user_name.place(x=53, y=90)
        self.user_name.focus()


        self.user_pass = customtkinter.CTkEntry(frame, width=220, height=32, 
                                           #textvariable=self.passwd_,
                                            placeholder_text='Enter your password',
                                            show='....', font=('Sans', 14))
        self.user_pass.place(x=53, y=150)


        forgot_password = customtkinter.CTkButton(frame, text='Forgot password', width=83, 
                                                height=20,corner_radius=5,
                                                font=customtkinter.CTkFont('Sans', 13),
                                                hover_color=('gray70', 'gray30'),
                                                fg_color='transparent',
                                                border_color='gray40',
                                                command=self.forgot_password_)
        forgot_password.place(x=155, y=203)


        signup_btn = customtkinter.CTkButton(frame, text='Signup', width=83, 
                                                height=20,corner_radius=5,
                                                font=customtkinter.CTkFont('Sans', 13),
                                                hover_color=('gray70', 'gray30'),
                                                fg_color='transparent',
                                                border_color='gray40',
                                                command=self.create_account)
        signup_btn.place(x=54, y=203)


        login_btn = customtkinter.CTkButton(frame, text='Login', width=220, 
                                                height=32,corner_radius=5,
                                                font=customtkinter.CTkFont('Sans', 13),
                                                hover_color=('#3CCF4E'),
                                                fg_color='transparent',
                                                border_color='gray40',
                                                border_width=0.6,
                                                command=self.admin_page)
        login_btn.place(x=54, y=250)


        alternative_btn = customtkinter.CTkButton(frame, text='Google', width=220, 
                                                height=32,corner_radius=5, image=logimage,
                                                font=customtkinter.CTkFont('Sans', 13),
                                                hover_color=('#3CCF4E'), compound='left',
                                                fg_color=('gray7', 'gray30'),
                                                border_color='gray40',
                                                border_width=0.6)
        alternative_btn.place(x=54, y=300)


        # self.login.mainloop()


    def create_account(self)-> None:
        register.UserSignup()
        self.login.destroy()


    def forgot_password_(self)-> None:
        self.login.destroy()
        forget_password.Passwordreset()


    def admin_page(self)-> None:
        usr = self.user_name.get().lower()
        psd = self.user_pass.get().lower()
        if usr in ('kenneth') and psd in ('mmmmm', 'mmm'):
            dashboard.Dashboard()
            self.login.destroy()
            CTkMessagebox(title='Welcome', message='Welcome to Daily Sales\n'
                            'Please remember to save your work', icon='check', 
                            option_1='Thanks')
        else:
            CTkMessagebox(title='Error', message='Username or password incorrect', 
                          icon='cancel', option_1='Ok')
            # if msg.get() == 'Yes':
            #     print('try again')
        



if __name__ == "__main__":
    app = LoginUser()

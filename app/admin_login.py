import os
from tkinter import *
import customtkinter
from PIL import Image
import admin_dashboard
import admin_signup, admin_forget



class Adminlogin(customtkinter.CTkToplevel):
    def __init__(self):
        # self.superlogin = customtkinter.CTk()
        self.superlogin = customtkinter.CTkToplevel()
        self.superlogin.title('[Admin login]')
        self.superlogin.resizable(0, 0)
        self.superlogin.geometry('500x500+400+100')
        icon_image_ = PhotoImage(file='app/icons/logo_02.png')
        self.superlogin.tk.call('wm', 'iconphoto', self.superlogin._w, icon_image_)


        self.superlogin.columnconfigure(0, weight=1, uniform='a')
        self.superlogin.rowconfigure(1, weight=0, uniform='a')


        image_path = os.path.join(os.path.dirname(os.path.relpath(__file__)), 
                                                                'icons')
        logimage = customtkinter.CTkImage(Image.open(os.path.join(image_path,
                                                                'Google__G__Logo.svg.webp')),
        size=(17, 17))


        self.background_image = PhotoImage(file='app/icons/pattern.png')
        self.background_label = Label(self.superlogin, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)


        frame = customtkinter.CTkFrame(self.superlogin, width=320, height=400, 
                                        corner_radius=10, 
                                        border_color='gray50')
        frame.pack(pady=60, anchor='center')
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure((0,1,2), weight=1)


        title_lable = customtkinter.CTkLabel(frame, text='Login.',
                                            font=customtkinter.CTkFont('Sans', 20)
                                            )
        title_lable.place(x=130, y=30)

        
        user_name = customtkinter.CTkEntry(frame, width=220, height=32,
                                            placeholder_text='Username',
                                            font=('Sans', 14)
                                            )
        user_name.place(x=53, y=90)
        user_name.focus()


        user_name = customtkinter.CTkEntry(frame, width=220, height=32,
                                            placeholder_text='Password',
                                            show='....', font=('Sans', 14)
                                            )
        user_name.place(x=53, y=150)


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
                                                command=self.create_account
                                                )
        signup_btn.place(x=54, y=203)


        superlogin_btn = customtkinter.CTkButton(frame, text='Login', width=220, 
                                                height=32,corner_radius=5,
                                                font=customtkinter.CTkFont('Sans', 13),
                                                hover_color=('#3CCF4E'),
                                                fg_color='transparent',
                                                border_color='gray40',
                                                border_width=0.6,
                                                command=self.admin_page
                                                )
        superlogin_btn.place(x=54, y=250)



        alternative_btn = customtkinter.CTkButton(frame, text='Google', width=220, 
                                                height=32,corner_radius=5, image=logimage,
                                                font=customtkinter.CTkFont('Sans', 13),
                                                hover_color=('#3CCF4E'), compound='left',
                                                fg_color=('gray7', 'gray30'),
                                                border_color='gray40',
                                                border_width=0.6
                                                )
        alternative_btn.place(x=54, y=300)

        # self.superlogin.mainloop()



    def create_account(self)-> None:
        admin_signup.Adminignup()
        self.superlogin.destroy()


    def forgot_password_(self)-> None:
        self.superlogin.destroy()
        admin_forget.Resetpassword()


    def admin_page(self)-> None:
        admin_dashboard.Adminsuper()
        self.superlogin.destroy()




if __name__ == "__main__":
    app = Adminlogin()

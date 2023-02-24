import os
import login
from tkinter import *
import customtkinter
from PIL import Image





class Adminignup(customtkinter.CTkToplevel):
    """This class returns the register or registration page whenever it is been called"""
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
                                            placeholder_text='Username',
                                            font=('Sans', 14)
                                            )
        user_name.place(x=53, y=70)
        user_name.focus()


        user_password = customtkinter.CTkEntry(frame, width=220, height=32,
                                            placeholder_text='Password', 
                                            show='....', font=('Sans', 14)
                                            )
        user_password.place(x=53, y=130)


        comfirm_password = customtkinter.CTkEntry(frame, width=220, height=32,
                                            placeholder_text='Comfirm_password', 
                                            show='....', font=('Sans', 14)
                                            )
        comfirm_password.place(x=53, y=190)


        register_btn = customtkinter.CTkButton(frame, text='register', width=220, 
                                                height=32,corner_radius=5,
                                                font=customtkinter.CTkFont('Sans', 13),
                                                hover_color=('#3CCF4E'),
                                                fg_color='transparent',
                                                border_color='gray40',
                                                border_width=0.6
                                                )
        register_btn.place(x=54, y=245)


        forgot_password = customtkinter.CTkButton(frame, text='Already have account? Login.', 
                                                height=20, width=100, corner_radius=5,
                                                font=customtkinter.CTkFont('Sans', 13),
                                                hover_color=('gray70', 'gray30'),
                                                fg_color='transparent',
                                                border_color='gray40',
                                                command=self.login_function
                                                )
        forgot_password.place(x=65, y=285)


        alternative_btn = customtkinter.CTkButton(frame, text='Register using google', width=220, 
                                                height=30,corner_radius=5, image=logimage,
                                                font=customtkinter.CTkFont('Sans', 13),
                                                hover_color=('#3CCF4E'), compound='left',
                                                fg_color=('gray7', 'gray30'),
                                                border_color='gray40',
                                                border_width=0.6
                                                )
        alternative_btn.place(x=54, y=320)

        # self.register.mainloop()


    def login_function(self)-> None:
        login.LoginUser()
        self.register.destroy()





if __name__ == "__main__":
    app = Adminignup()

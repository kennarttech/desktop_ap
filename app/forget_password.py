import os
from tkinter import *
import customtkinter
from PIL import Image
import register, login



class Passwordreset(customtkinter.CTk):
    def __init__(self):
        # self.password_reset = customtkinter.CTk()
        self.password_reset = customtkinter.CTkToplevel()
        self.password_reset.title('[Password Reset]')
        self.password_reset.resizable(0, 0)
        self.password_reset.geometry('500x500+400+100')
        icon_image_ = PhotoImage(file='app/icons/logo_02.png')
        self.password_reset.tk.call('wm', 'iconphoto', self.password_reset._w, icon_image_)


        self.password_reset.columnconfigure(0, weight=1, uniform='a')
        self.password_reset.rowconfigure(1, weight=0, uniform='a')


        image_path = os.path.join(os.path.dirname(os.path.relpath(__file__)), 
                                                'icons')
        logimage = customtkinter.CTkImage(Image.open(os.path.join(image_path, 
                                        'Google__G__Logo.svg.webp')),
        size=(17, 17))
        background_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, 
                                                'pattern.png')),
        size=(900, 600))


        self.background_image = PhotoImage(file='app/icons/pattern.png')
        self.background_label = Label(self.password_reset, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)


        frame = customtkinter.CTkFrame(self.password_reset, width=320, height=400, 
                                        corner_radius=10, 
                                        border_color='gray50')
        frame.pack(pady=60, anchor='center')
        frame.grid_columnconfigure((0,1,2), weight=0)
        frame.grid_rowconfigure((0,1,2), weight=1)


        title_lable = customtkinter.CTkLabel(frame, text='Reset password',
                                            font=customtkinter.CTkFont('Sans', 20)
                                            )
        title_lable.place(x=75, y=30)

        
        user_name = customtkinter.CTkEntry(frame, width=220, height=32,
                                            placeholder_text='New password',
                                            font=('Sans', 14)
                                            )
        user_name.place(x=53, y=90)
        user_name.focus()


        user_name = customtkinter.CTkEntry(frame, width=220, height=32,
                                            placeholder_text='Comfirm_Password',
                                            show='....', font=('Sans', 14)
                                            )
        user_name.place(x=53, y=150)


        login_btn = customtkinter.CTkButton(frame, text='Reset', width=220, 
                                                height=32,corner_radius=5,
                                                font=customtkinter.CTkFont('Sans', 13),
                                                hover_color=('#3CCF4E'),
                                                fg_color='transparent',
                                                border_color='gray40',
                                                border_width=0.6,
                                                command=self.new_password
                                                )
        login_btn.place(x=54, y=210)



        alternative_btn = customtkinter.CTkButton(frame, text='Reset password using Google', width=220, 
                                                height=32,corner_radius=5, image=logimage,
                                                font=customtkinter.CTkFont('Sans', 12),
                                                hover_color=('#3CCF4E'), compound='left',
                                                fg_color=('gray7', 'gray30'),
                                                border_color='gray40',
                                                border_width=0.6
                                                )
        alternative_btn.place(x=54, y=275)

        # self.password_reset.mainloop()



    def new_password(self):
        login.LoginUser()
        self.password_reset.destroy()




if __name__ == "__main__":
    app = Passwordreset()

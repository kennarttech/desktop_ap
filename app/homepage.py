"""This are built-in modules, which are part of the Python Standard Library"""
import os
import json
from tkinter import *
from PIL import Image


"""this are third-party modules that need to be installed separately using pip"""
import customtkinter
from tktooltip import ToolTip
from CTkMessagebox import CTkMessagebox


"""This are local modules that I have created myself and are part of the project."""
import login
import about
import admin_login


class Homepage(customtkinter.CTk):
    """This class defines the homepage, that is use create the GUI"""


    customtkinter.set_appearance_mode('system')
    customtkinter.set_default_color_theme("green")


    """Using contex manager to load json file that is use the home page"""
    Text = 'app/config/settings.json'

    with open(file=Text, mode='r', encoding='utf-8') as rf:
        text = json.load(rf)


    def __init__(self, master) -> None:
        self.master = master
        self.master.columnconfigure(0, weight = 1, uniform='a')
        self.master.rowconfigure((1,2,3,4), weight = 1, uniform='a')


        self.image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icons")
        self.home_logo = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "logo_07.png")), 
        size=(17, 17))


        self.background_image = PhotoImage(file='app/icons/logo_15.png')
        self.background_label = Label(self.master, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)


        top_frame = customtkinter.CTkFrame(self.master, 
                                            border_width = 0.6, 
                                            border_color ='gray10',
                                            height = 60,
                                            fg_color='#06283D',
                                            corner_radius = 3)
        top_frame.grid(row = 0, column = 0, ipady=(3), sticky = NSEW)
        top_frame.grid_columnconfigure((0,1,2,3,4), weight = 1)


        home_button1 = customtkinter.CTkButton(top_frame, text='Home', height=20, 
                                                font=('Roboto', 13), width=50, 
                                                hover_color=("gray70", "gray30"),
                                                corner_radius=5, image=self.home_logo, 
                                                fg_color="transparent", compound='left',
                                                text_color=("gray10", "gray90"),
                                                border_color='gray40',border_width=1)
        home_button1.grid(row=0, column=0, padx=(20, 10), pady=(7, 0), sticky=W)


        daily_record_button = customtkinter.CTkButton(top_frame, text='Daily Record', 
                                                font=('Roboto', 13), width=85, 
                                                height=20, hover_color=("gray70", "gray30"),
                                                corner_radius=5,fg_color="transparent", 
                                                text_color=("gray10", "gray90"),
                                                border_color='gray40',border_width=1,
                                                command=self.dsales)
        daily_record_button.grid(row=0, column=2, padx=(0, 35), pady=(7, 0), sticky=N)
        ToolTip(daily_record_button, fg='white', bg='gray15', msg='Daily record')


        about_button = customtkinter.CTkButton(top_frame, text='About', 
                                            font=customtkinter.CTkFont('Roboto', 13),
                                            hover_color=("gray70", "gray30"), corner_radius=5, 
                                            width=50, height=20, fg_color="transparent", 
                                            text_color=("gray10", "gray90"),
                                            border_color='gray40',border_width=1,
                                            command=self.about_page)
        about_button.grid(row=0, column=2, padx=(150, 35), pady=(7, 0), sticky=N)
        ToolTip(about_button, msg='About Us', fg='white', bg='gray15', delay=0)


        login_button = customtkinter.CTkButton(top_frame, text='Admin only', 
                                            font=('Roboto', 13), corner_radius=5,
                                            width=70, hover_color=("gray70", "gray30"),
                                            fg_color="transparent", height=20, 
                                            text_color=("gray10", "gray90"),
                                            border_color='gray40',border_width=1,
                                            hover=True, command=self.create_account)
        login_button.grid(row=0, column=4, padx=(0, 18), pady=(7, 0), sticky=E)
        ToolTip(login_button, msg='Please Login or Signup', fg='white', bg='gray15')


        middle_frame = customtkinter.CTkFrame(self.master, border_width=0.6,
                                              border_color='gray10', 
                                              fg_color='#06283D', corner_radius=5)
        middle_frame.grid(row=4, column=0, padx=(0, 0), pady=(130, 0), sticky='nsew')
        middle_frame.grid_columnconfigure((0,1,2), weight=1)
        middle_frame.grid_rowconfigure((0,1,2), weight=1)


        welcome_label = customtkinter.CTkLabel(master=middle_frame, 
                                               text=self.text['footer'],
                                               font=('Sans', 15),)
        welcome_label.grid(row=0, column=1, padx=5, pady=5)


    def dsales(self)-> None:
        msg = CTkMessagebox(title='Login', message='Please Signup/Login \n'
                            'to access this page', icon='warning', option_1='Ok',
                            option_2='Cancel')
        if msg.get() == 'Ok':
            self.master.withdraw()
            login.LoginUser()
        else:
            return self.master
        

    def create_account(self)-> None:
        admin_login.Adminlogin()
        self.master.withdraw()

        
    def about_page(self)-> None:
        about.Aboutpage()



def main():
    """this function define the attribute of the GUI and also create the the GUI"""
    home = customtkinter.CTk()
    Homepage(home)
    home.title('Home Page')
    home.minsize(900, 500)
    home.geometry('500x500+200+100')
    home.attributes('-zoomed', True)
    home.attributes('-alpha', 0.7)
    icon_image = PhotoImage(file='app/icons/logo_04.png')
    home.tk.call('wm', 'iconphoto', home._w, icon_image)
    home.mainloop()



if __name__ == "__main__":
    app = main()
    print(Homepage.__doc__)


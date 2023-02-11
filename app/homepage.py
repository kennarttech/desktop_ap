import os
from tkinter import *
import customtkinter
from PIL import Image
import login, about





class Homepage(customtkinter.CTk):
    """This is class loads the home page when it is been called"""

    customtkinter.set_appearance_mode('system')
    customtkinter.set_default_color_theme("green")


    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icons")
    home_logo = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo_07.png")), size=(17, 17))
    

    def __init__(self, master) -> None:
        self.master = master
        self.master.columnconfigure(0, weight = 1, uniform='a')
        self.master.rowconfigure(1, weight = 0, uniform='a')


        top_frame = customtkinter.CTkFrame(self.master, 
                                            border_width = 0.6, 
                                            border_color ='gray10',
                                            height = 60,
                                            corner_radius = 3)
        top_frame.grid(row = 0, column = 0, ipady=(3), sticky = NSEW)
        top_frame.grid_columnconfigure((0,1,2,3,4), weight = 1)


        home_button1 = customtkinter.CTkButton(top_frame, text='Home', height=20, 
                                                font=('Roboto', 13), width=50, 
                                                hover_color=("gray70", "gray30"),
                                                corner_radius=5, image=self.home_logo, 
                                                compound='left',
                                                fg_color="transparent", 
                                                text_color=("gray10", "gray90"),
                                                border_color='gray40',border_width=1)
        home_button1.grid(row=0, column=0, padx=(20, 10), pady=(7, 0), sticky=W)


        daily_record_button = customtkinter.CTkButton(top_frame, text='Daily Record', 
                                                font=('Roboto', 13), width=83, 
                                                height=20, hover_color=("gray70", "gray30"),
                                                corner_radius=5,fg_color="transparent", 
                                                text_color=("gray10", "gray90"),
                                                border_color='gray40',border_width=1,
                                                command=None)
        daily_record_button.grid(row=0, column=2, padx=(0, 0), pady=(7, 0), sticky=N)


        about_button = customtkinter.CTkButton(top_frame, text='About', 
                                            font=customtkinter.CTkFont('Roboto', 13),
                                            hover_color=("gray70", "gray30"), corner_radius=5, 
                                            width=50, height=20, fg_color="transparent", 
                                            text_color=("gray10", "gray90"),
                                            border_color='gray40',border_width=1,
                                            command=self.about_page)
        about_button.grid(row=0, column=2, padx=(150, 0), pady=(7, 0), sticky=N)


        login_button = customtkinter.CTkButton(top_frame, text='Login/Signup', 
                                            font=('Roboto', 13), height=20, corner_radius=5,
                                            width=65, hover_color=("gray70", "gray30"),
                                            fg_color="transparent", 
                                            text_color=("gray10", "gray90"),
                                            border_color='gray40',border_width=1,
                                            hover=True, command=self.create_account)
        login_button.grid(row=0, column=4, padx=(0, 20), pady=(7, 0), sticky=E)



    def create_account(self):
        login.LoginUser()
        self.master.iconify()



    def about_page(self):
        about.Aboutpage()





def main():
    home = customtkinter.CTk()
    app = Homepage(home)
    home.title('Home Page')
    home.minsize(440, 400)
    home.geometry('500x500+400+100')
    home.attributes('-zoomed', True)
    icon_image = PhotoImage(file='app/icons/logo_04.png')
    home.tk.call('wm', 'iconphoto', home._w, icon_image)
    home.mainloop()



if __name__ == "__main__":
    app = main()


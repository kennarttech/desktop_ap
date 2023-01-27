import os
from tkinter import *
import customtkinter
from PIL import Image




class Homepage(customtkinter.CTk):
    """This is class loads the home page when it is been called"""

    customtkinter.set_appearance_mode('system')
    customtkinter.set_default_color_theme("green")
    customtkinter.set_window_scaling(1)
    

    def __init__(self, master) -> None:
        self.master = master
        self.master.columnconfigure(0, weight = 1)
        self.master.columnconfigure(1, weight = 0, uniform='a')
        self.master.rowconfigure(1, weight = 1)


        top_frame = customtkinter.CTkFrame(self.master, 
                                            border_width = 0.6, 
                                            border_color ='gray10',
                                            height = 60,
                                            corner_radius = 3)
        top_frame.grid(row = 0, column = 0, ipady=(2), sticky = NSEW)
        top_frame.grid_columnconfigure(0, weight = 1)


        footer_frame = customtkinter.CTkFrame(self.master, 
                                            border_width = 0.6, 
                                            border_color ='gray10',
                                            height = 1,
                                            fg_color='gray25',
                                            corner_radius = 3)
        footer_frame.grid(row = 2, column = 0, sticky=EW)
        footer_frame.grid_rowconfigure(0, weight = 1)


        logo_label = customtkinter.CTkLabel(top_frame, text = 'DS ENTERPRISE', 
                                            font=('Roboto', 13))
        logo_label.grid(row = 0, column=0, padx=(20, 100), pady=(10, 10), sticky=W)


        home_button1 = customtkinter.CTkButton(top_frame, text='Home', height=20, 
                                                font=('Roboto', 13), width=50, 
                                                hover_color=("gray70", "gray30"),
                                                corner_radius=5,
                                                fg_color="transparent", 
                                                text_color=("gray10", "gray90"),
                                                border_color='gray40',border_width=1)
        home_button1.grid(row=0, column=0, padx=(1, 120), pady=(12, 0), sticky=N)


        daily_record_button = customtkinter.CTkButton(top_frame, text='Daily Record', 
                                                font=('Roboto', 13), width=83, 
                                                height=20, hover_color=("gray70", "gray30"),
                                                corner_radius=5,fg_color="transparent", 
                                                text_color=("gray10", "gray90"),
                                                border_color='gray40',border_width=1)
        daily_record_button.grid(row=0, column=0, padx=(35, 8), pady=(12, 0), sticky=N)


        about_button = customtkinter.CTkButton(top_frame, text='About', 
                                            font=customtkinter.CTkFont('Roboto', 13),
                                            hover_color=("gray70", "gray30"), corner_radius=5, 
                                            width=50, height=20, fg_color="transparent", 
                                            text_color=("gray10", "gray90"),
                                            border_color='gray40',border_width=1,
                                            hover=False, command=self.about_page)
        about_button.grid(row=0, column=0, padx=(180, 8), pady=(12, 0), sticky=N)


        login_button = customtkinter.CTkButton(top_frame, text='Login/Signup', 
                                            font=('Roboto', 13), height=20, corner_radius=5,
                                            width=65, hover_color=("gray70", "gray30"),
                                            fg_color="transparent", 
                                            text_color=("gray10", "gray90"),
                                            border_color='gray40',border_width=1,
                                            hover=True)
        login_button.grid(row=0, column=0, padx=(5, 20), pady=(0, 0), sticky=E)


        footer_text = customtkinter.CTkLabel(footer_frame, text='About Us', 
                                            font=customtkinter.CTkFont('Times', 18))
        footer_text.grid(row=0, column=0, padx=(30), pady=(10, 4), sticky=W)

        footer_text2 = customtkinter.CTkLabel(footer_frame, text="All Right Reserved 2023 @ DS Print")
        footer_text2.grid(row=0, column=1, padx=(400), pady=(0, 5), sticky=S)







    def about_page(self):
        self.master.withdraw()
        os.system('python app/about.py')
        self.master.destroy()





def main():
    home = customtkinter.CTk()
    app = Homepage(home)
    home.title('Home Page')
    home.minsize(620, 500)
    home.geometry('1364x690+7+10')
    icon_image = PhotoImage(file='app/icons/AA.png')
    home.tk.call('wm', 'iconphoto', home._w, icon_image)
    home.mainloop()


if __name__ == "__main__":
    app = main()

    

    

import os
from tkinter import *
import customtkinter



class Homepage(customtkinter.CTk):
    """This is class loads the home page when it is been called"""

    customtkinter.set_appearance_mode('system')
    customtkinter.set_window_scaling(1)


    def __init__(self, master) -> None:
        self.master = master
        self.master.columnconfigure(0, weight = 1)
        self.master.columnconfigure(1, weight = 0)
        self.master.rowconfigure(1, weight = 1)


        top_frame = customtkinter.CTkFrame(self.master, 
                                            border_width = 0.6, 
                                            border_color ='gray10',
                                            height = 60,
                                            corner_radius = 3)
        top_frame.grid(row = 0, column = 0, sticky = NSEW)
        top_frame.grid_columnconfigure(0, weight = 1)


        logo_label = customtkinter.CTkLabel(top_frame, text = 'DS ENTERPRISE', 
                                            font=('Times', 18))
        logo_label.grid(row = 0, column=0, padx=(20, 100), pady=(20, 10), sticky=W)


        home_button1 = customtkinter.CTkButton(top_frame, text='Home', height=25, 
                                                font=('Times', 20), width=80, 
                                                hover_color=("gray70", "gray30"))
        home_button1.grid(row=0, column=0, padx=(1, 120), pady=(15, 0), sticky=N)


        daily_record_button = customtkinter.CTkButton(top_frame, text='Daily Record', 
                                                font=('Times', 20), width=100, 
                                                height=25, hover_color=("gray70", "gray30"))
        daily_record_button.grid(row=0, column=0, padx=(100, 8), pady=(15, 0), sticky=N)


        about_button = customtkinter.CTkButton(top_frame, text='About', 
                                            font=customtkinter.CTkFont('Times', 20),
                                            hover_color=("gray70", "gray30"), width=65,
                                            height=25)
        about_button.grid(row=0, column=0, padx=(300, 8), pady=(15, 0), sticky=N)


        login_button = customtkinter.CTkButton(top_frame, text='Login/Signup', 
                                            font=('Times', 20), height=25,
                                            width=65, hover_color=("gray70", "gray30"))
        login_button.grid(row=0, column=0, padx=(5, 40), pady=(0, 0), sticky=E)



        





def main():
    home = customtkinter.CTk()
    app = Homepage(home)
    home.title('Home Page')
    home.minsize(700, 500)
    home.geometry('1240x600+50+40')
    icon_image = PhotoImage(file='app/icons/AA.png')
    home.tk.call('wm', 'iconphoto', home._w, icon_image)

    home.mainloop()


if __name__ == "__main__":
    app = main()

    

    

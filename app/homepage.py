import os
from tkinter import *
import customtkinter



class Homepage(customtkinter.CTk):
    """This is class loads the home page when it is been called"""
    customtkinter.set_appearance_mode('')

    def __init__(self, master) -> None:
        self.master = master

        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=0)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=0)



        label = customtkinter.CTkLabel(self.master, text='Welcome to DS Enterprice',
                                     font=('Times', 40))
        label.grid()





def main():
    home = customtkinter.CTk()
    app = Homepage(home)
    home.title('Home Page')
    home.geometry('800x500+300+130')
    home.mainloop()


if __name__ == "__main__":
    app = main()

    

    

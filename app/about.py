import os
from tkinter import *
import customtkinter




class aboutpage(customtkinter.CTk):
    """This is class loads the about page when it is been called"""

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


        footer_frame = customtkinter.CTkFrame(self.master, 
                                            border_width = 0.6, 
                                            border_color ='gray10',
                                            height = 60,
                                            corner_radius = 3)
        footer_frame.grid(row = 1, column = 0, sticky=EW)
        footer_frame.grid_rowconfigure(0, weight = 1)







    # def about_page(self):
    #     self.about.withdraw()
    #     os.system('python app/about.py')
    #     self.about.destroy()




def main():
    about = customtkinter.CTk()
    app = aboutpage(about)
    about.title('about Page')
    about.minsize(700, 500)
    about.geometry('1240x600+50+40')
    icon_image = PhotoImage(file='app/icons/AA.png')
    about.tk.call('wm', 'iconphoto', about._w, icon_image)
    about.mainloop()


if __name__ == "__main__":
    app = main()

    

    

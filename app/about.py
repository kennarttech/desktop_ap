import os
# import random 
from tkinter import *
import customtkinter





class Aboutpage(customtkinter.CTk):
    """This is class loads the about page when it is been called"""

    customtkinter.set_appearance_mode('system')
    customtkinter.set_window_scaling(0.6)


    TEXT_FILE_PATH = "app/history.txt"
    with open(file=TEXT_FILE_PATH, mode='r') as rf:
        for i in rf.read():
            result = i
            # print(result, end='')


    def __init__(self, master) -> None:
        self.master = master
        self.master.columnconfigure(0, weight = 1, uniform='a')
        self.master.columnconfigure(1, weight = 0)
        self.master.rowconfigure(1, weight = 1)


        about_top_frame = customtkinter.CTkFrame(self.master, 
                                            border_width = 0.6, 
                                            border_color ='gray10',
                                            corner_radius = 3)
        about_top_frame.grid(row = 0, column = 0, sticky = NSEW)
        about_top_frame.grid_columnconfigure(0, weight = 1)


        home_button1 = customtkinter.CTkButton(about_top_frame, text='Back home /Exit', 
                                                height=20, 
                                                font=('Roboto', 13), width=80, 
                                                hover_color=("gray70", "gray30"), 
                                                corner_radius=5, command=self.backhome)
        home_button1.grid(row=2, column=0, padx=(18, 25), pady=(12, 12), sticky=N)


        default_textbox = customtkinter.CTkTextbox(self.master, width=250, font=('Times', 20),
                                                    text_color=('gray80'), corner_radius=10,
                                                    scrollbar_button_color=('teal'),
                                                    scrollbar_button_hover_color=('red'))
        default_textbox.grid(row=1, column=0, padx=(2, 0), pady=(80, 30), sticky="nsew")
        default_textbox.insert(0.0, 'About DS Enterprise\n\n'+ "The printing press is a machine that was invented in the 15th century by Johannes Gutenberg, a German blacksmith and goldsmith. It revolutionized the way books were produced by allowing for the mass production of printed materials. Prior to the invention of the printing press, books were hand-copied by monks, which made them expensive and rare.\n\nGutenberg's printing press used movable type, which allowed for individual letters and characters to be set into a frame and then pressed onto paper, creating a printed page. This process was much faster and more efficient than hand-copying, and it made books and other printed materials more affordable and widely available.\n\nThe printing press quickly spread throughout Europe and soon the world, and it played a significant role in the spread of knowledge, ideas, and information during the Renaissance and beyond. Today, the printing press continues to be an important tool for the production of books, newspapers, magazines, and other printed materials.")
        default_textbox.configure(state='disable')


        footer_frame = customtkinter.CTkFrame(self.master, 
                                            border_width = 0.6, 
                                            border_color ='gray10',
                                            height = 30, fg_color='gray25',
                                            corner_radius = 3)
        footer_frame.grid(row = 2, column = 0, sticky=EW)
        footer_frame.grid_rowconfigure(0, weight = 1)






    def backhome(self):
        self.master.withdraw()
        os.system('python app/homepage.py')
        self.master.destroy()




def main():
    about = customtkinter.CTk()
    app = Aboutpage(about)
    about.title('About Page')
    about.resizable(0, 0)
    about.geometry('1240x800+300+100')
    icon_image = PhotoImage(file='app/icons/AA.png')
    about.tk.call('wm', 'iconphoto', about._w, icon_image)
    about.mainloop()


if __name__ == "__main__":
    app = main()

    

    

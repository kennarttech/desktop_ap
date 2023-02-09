import os
from tkinter import *
import customtkinter
import homepage




class Aboutpage(customtkinter.CTk):
    """This is class loads the about page when it is been called"""

    customtkinter.set_appearance_mode('system')


    TEXT_FILE_PATH = "app/readme_reference/history.txt"

    with open(file=TEXT_FILE_PATH, mode='r') as rf:
        for i in rf.read():
            result = i
            # print(result, end='')



    def __init__(self) -> None:
        # self.about = customtkinter.CTk()
        self.about = customtkinter.CTkToplevel()
        self.about.title('About Page')
        self.about.attributes('-zoomed', True)
        self.about.geometry('900x500+250+100')
        icon_image = PhotoImage(file='app/icons/AA.png')
        self.about.tk.call('wm', 'iconphoto', self.about._w, icon_image)
      


        self.about.columnconfigure(0, weight = 1, uniform='a')
        self.about.columnconfigure(1, weight = 0)
        self.about.rowconfigure(1, weight = 1)



        about_top_frame = customtkinter.CTkFrame(self.about, 
                                            border_width = 0.6, 
                                            border_color ='gray10',
                                            corner_radius = 3)
        about_top_frame.grid(row = 0, column = 0, sticky = NSEW)
        about_top_frame.grid_columnconfigure(0, weight = 1)



        home_button1 = customtkinter.CTkButton(about_top_frame, text='Back home /Exit', 
                                                height=20, 
                                                font=('Roboto', 13), width=80, 
                                                hover_color=("gray70", "gray30"), 
                                                corner_radius=5, command=self.backhome,
                                                fg_color="transparent", 
                                                text_color=("gray10", "gray90"),
                                                border_color='gray40',border_width=1)
        home_button1.grid(row=2, column=0, padx=(18, 25), pady=(12, 12), sticky=N)



        default_textbox = customtkinter.CTkTextbox(self.about, width=250, font=('Times', 20),
                                                    text_color=('gray80'), corner_radius=10,
                                                    scrollbar_button_color=('teal'),
                                                    scrollbar_button_hover_color=('red'))
        default_textbox.grid(row=1, column=0, padx=(2, 0), pady=(80, 30), sticky="nsew")
        default_textbox.insert(0.0, 'About DS Enterprise\n\n'+ "The printing press is a machine that was invented in the 15th century by Johannes Gutenberg, newspapers, magazines, and other printed materials.")
        default_textbox.configure(state='disable')


        footer_frame = customtkinter.CTkFrame(self.about, 
                                            border_width = 0.6, 
                                            border_color ='gray10',
                                            height = 30, fg_color='gray25',
                                            corner_radius = 3)
        footer_frame.grid(row = 2, column = 0, sticky=EW)
        footer_frame.grid_rowconfigure(0, weight = 1)

        # self.about.mainloop()




    def backhome(self):
        self.about.withdraw()
        homepage.Homepage()
        self.about.deiconify()




if __name__ == "__main__":
    app = Aboutpage()
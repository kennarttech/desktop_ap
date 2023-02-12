import os, sys
import homepage
from tkinter import *
import customtkinter
from PIL import Image



class Dashboard(customtkinter.CTkToplevel):

    customtkinter.set_appearance_mode('system')
    customtkinter.set_default_color_theme('green')

    def __init__(self) -> None:
        self.dash = customtkinter.CTk()
        # self.dash = customtkinter.CTkToplevel()
        self.dash.attributes('-zoomed', True)
        self.dash.geometry('1000x600+155+50')
        self.dash.title('Dashboard')


        self.icon_image = PhotoImage(file='app/icons/logo_03.png')
        self.dash.tk.call('wm', 'iconphoto', self.dash._w, self.icon_image)


        self.dash.columnconfigure((1,2), weight=1, uniform='a')
        self.dash.rowconfigure(0, weight=1, uniform='a')

        left_frame = customtkinter.CTkFrame(master=self.dash, 
                                            border_color='gray10', 
                                            border_width=0.8,
                                            fg_color='gray25', 
                                            corner_radius=5,
                                            # width=500
                                            )
        left_frame.grid(row=0, column=0, ipadx=(30), pady=(0,0), sticky=NSEW)
        left_frame.grid_rowconfigure(5, weight=1)


        status_label = customtkinter.CTkLabel(left_frame, text='Welcome,\n[00121]',
                                              font=customtkinter.CTkFont('Roboto', 20),
                                              text_color='#16FF00')
        status_label.grid(row=1, column=0, padx=20, pady=30, sticky=EW)     

        
        
        



    # status_label = customtkinter.CTkLabel(left_frame, text='Welcome,\n00211422',
    #                                           font=customtkinter.CTkFont('Sans', 15))
    #     status_label.grid(row=2, column=0,padx=20, pady=30, sticky=EW) 


        self.dash.mainloop()








if __name__ == "__main__":
    app = Dashboard()


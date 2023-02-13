import os, sys
import homepage
from tkinter import *
import customtkinter
from PIL import Image
from tkinter import messagebox


class Dashboard(customtkinter.CTkToplevel):

    customtkinter.set_appearance_mode('system')
    customtkinter.set_default_color_theme('green')

    def __init__(self) -> None:
        # self.dash = customtkinter.CTk()
        self.dash = customtkinter.CTkToplevel()
        self.dash.attributes('-zoomed', True)
        self.dash.geometry('1000x600+155+50')
        self.dash.title('Dashboard')


        self.icon_image = PhotoImage(file='app/icons/logo_03.png')
        self.dash.tk.call('wm', 'iconphoto', self.dash._w, self.icon_image)


        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'icons')
        user_profile_logo = customtkinter.CTkImage(Image.open(os.path.join(image_path,'logo_12.png')), 
        size=(130, 130))

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'icons')
        new_frames = customtkinter.CTkImage(Image.open(os.path.join(image_path,'logo_10.png')),
        size=(30, 30))

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'icons')
        daily_sales = customtkinter.CTkImage(Image.open(os.path.join(image_path,'logo_14.png')),
        size=(30, 30))

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'icons')
        back_home = customtkinter.CTkImage(Image.open(os.path.join(image_path, 'logo_07.png')), size=(30, 30))


        self.dash.columnconfigure((1,2), weight=1, uniform='a')
        self.dash.rowconfigure(0, weight=1, uniform='a')

        left_frame = customtkinter.CTkFrame(master=self.dash, 
                                            border_color='gray10', 
                                            border_width=0.8,
                                            fg_color='gray25', 
                                            corner_radius=5,
                                            # width=500
                                            )
        left_frame.grid(row=0, column=0, ipadx=(10), pady=(0,0), sticky=NSEW)
        left_frame.grid_rowconfigure(5, weight=1)


        user_profile = customtkinter.CTkLabel(master=left_frame, 
                                              text='\n\n\n\nProfile',      image=user_profile_logo,
                                              font=customtkinter.CTkFont('Roboto', 18),
                                              text_color='gray12')
        user_profile.grid(row=0, column=0, padx=20, pady=5, sticky=NSEW)


        status_label = customtkinter.CTkLabel(master=left_frame, text='Welcome,\n[00121]',
                                              font=customtkinter.CTkFont('Roboto', 20),
                                              text_color='#16FF00')
        status_label.grid(row=1, column=0, padx=30, pady=10, sticky=EW)     


        new_frame_button = customtkinter.CTkButton(master=left_frame, text='New Frames',
                                                   text_color=("gray10", "gray90"), fg_color='transparent',
                                                   hover_color=("gray70", "gray30"), 
                                                   height=30, width=30,
                                                   corner_radius=4, border_width=1,
                                                   image=new_frames, anchor='w')
        new_frame_button.grid(row=2, column=0, padx=10, pady=25, sticky=EW)


        daily_sales_button = customtkinter.CTkButton(master=left_frame, text='Daily Sales',
                                                   text_color=("gray10", "gray90"), fg_color='transparent',
                                                   hover_color=("gray70", "gray30"), 
                                                   height=30, width=30,
                                                   corner_radius=4, border_width=1,
                                                   image=daily_sales, anchor='w')
        daily_sales_button.grid(row=3, column=0, padx=10, pady=0, sticky=EW)


        exit_button = customtkinter.CTkButton(master=left_frame, text='  Exit',
                                                   text_color=("gray10", "gray90"), fg_color='transparent',
                                                   hover_color=("gray70", "gray30"), 
                                                   height=30, width=100, anchor='S',
                                                   corner_radius=4, border_width=1,
                                                   font=('Roboto', 18),image=back_home,
                                                   command=self.dashexit)
        exit_button.grid(row=5,  padx=1, pady=50, sticky='s')


        top_frame = customtkinter.CTkFrame(master=self.dash, border_width=0.6,
                                           border_color='gray10', fg_color='gray25',
                                           corner_radius=3, height=40)
        top_frame.grid(row=0, column=1, columnspan=2, padx=(0, 0), pady=(0, 400), 
                       ipadx=(400), ipady=(0), sticky=NSEW)
        top_frame.grid_columnconfigure(1, weight=1)
        

        # self.dash.mainloop()


    def dashexit(self):
        homepage.Homepage(self.dash)
        self.dash.destroy()
        sys.exit()
        







if __name__ == "__main__":
    app = Dashboard()


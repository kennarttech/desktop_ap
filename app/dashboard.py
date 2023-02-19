import json
import os, sys
import homepage
from tkinter import *
import customtkinter
from PIL import Image
from tktooltip import ToolTip
from tkinter import messagebox




class Dashboard(customtkinter.CTkToplevel):

    customtkinter.set_appearance_mode('system')
    customtkinter.set_default_color_theme('green')

    """Using context manager to open the a json file"""
    with open(file='app/config_files/names.json', mode='r') as settings_rf:
        user_data = json.load(settings_rf)

    def __init__(self) -> None:
        # self.dash = customtkinter.CTk()
        self.dash = customtkinter.CTkToplevel()
        self.dash.minsize(400, 430)
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
        
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'icons')
        search_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, 'logo_08.png')), size=(22, 22))


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
        left_frame.grid_rowconfigure((0,1,2,3,4,5), weight=1)


        user_profile = customtkinter.CTkLabel(master=left_frame, 
                                              text='\n\n\n\nProfile',      image=user_profile_logo,
                                              font=customtkinter.CTkFont('Roboto', 18),
                                              text_color='gray12')
        user_profile.grid(row=0, column=0, padx=20, pady=1, sticky=NSEW)


        
        status_label = customtkinter.CTkLabel(master=left_frame, text='Welcome,\n[00121]',
                                              font=customtkinter.CTkFont('Roboto', 20),
                                              text_color='#16FF00')
        status_label.grid(row=1, column=0, padx=30, ipady=2, sticky=EW)     


        new_frame_button = customtkinter.CTkButton(master=left_frame, text='New Frames',
                                                   text_color=("gray10", "gray90"), fg_color='transparent',
                                                   hover_color=("gray70", "gray30"), 
                                                   height=25, width=30,
                                                   corner_radius=4, border_width=1,
                                                   image=new_frames, anchor='w')
        new_frame_button.grid(row=2, column=0, padx=10, pady=2, sticky=EW)
        ToolTip(new_frame_button, msg='Upload new frames', fg='white', bg='gray15', delay=0)


        daily_sales_button = customtkinter.CTkButton(master=left_frame, text='Daily Sales',
                                                   text_color=("gray10", "gray90"), fg_color='transparent',
                                                   hover_color=("gray70", "gray30"), 
                                                   height=25, width=30,
                                                   corner_radius=4, border_width=1,
                                                   image=daily_sales, anchor='w')
        daily_sales_button.grid(row=3, column=0, padx=10, pady=0, sticky=EW)
        ToolTip(daily_sales_button, msg='New daily sales', fg='white', bg='gray15', delay=0)


        exit_button = customtkinter.CTkButton(master=left_frame, text='  Exit/Logout',
                                                   text_color=("white"), fg_color='teal',
                                                   hover_color=("gray70", "gray30"), 
                                                   height=25, width=100, anchor='S',
                                                   corner_radius=4, border_width=1,
                                                   font=('Roboto', 18),image=back_home,
                                                   command=self.dashexit)
        exit_button.grid(row=4,  padx=1, pady=50, sticky='s')
        ToolTip(exit_button, msg='Exit the program', fg='white', bg='gray15', delay=0)


        """This column downwards defines top, middle and down frames"""
        self.menu_frame = customtkinter.CTkFrame(master=self.dash, border_width=0.6,
                                           border_color='gray10', fg_color='gray28',
                                           corner_radius=5, width=1200, height=40)
        self.menu_frame.grid(row=0, column=1, columnspan=2, padx=(20,20), pady=(0, 12), sticky=N)
        self.menu_frame.grid_columnconfigure((0,1,2,3), weight=1)
        

        middle_frame = customtkinter.CTkFrame(master=self.dash, border_width=0.6,
                                           border_color='gray10', fg_color='gray28',
                                           corner_radius=5, width=1200, height=100)
        middle_frame.grid(row=0, column=1, columnspan=2, padx=(20,20), pady=(60, 60), sticky=NSEW)
        middle_frame.grid_columnconfigure((0,1,2,3), weight=1)

        label = customtkinter.CTkLabel(master=middle_frame, text=self.user_data['DS_Enterprise'],
                                       font=customtkinter.CTkFont('Sans', 20))
        label.grid(row=0, column=1, padx=(100, 2), pady=10)


        buttom_frame = customtkinter.CTkFrame(master=self.dash, border_width=0.6,
                                              border_color='gray10', fg_color='gray24',
                                              corner_radius=4, width=1200, height=25)
        buttom_frame.grid(row=0, column=1, columnspan=5, pady=(0, 0), sticky=S)
        buttom_frame.grid_columnconfigure((0,1,2,3), weight=1)
        """End of the frames"""

        menu_frame_label = customtkinter.CTkLabel(master=self.menu_frame, 
                                                  text='DS Collection System',
                                                  text_color='orange', font=('Sans', 15),
                                                  )
        menu_frame_label.place(x=40, y=20, anchor='w')


        search_box = customtkinter.CTkEntry(master=self.menu_frame, 
                                            placeholder_text='Search for deposite/name.....',
                                            width=220)
        search_box.place(x=560, y=20, anchor='e')
        ToolTip(search_box, msg='Search for anything', delay=0)

        
        search_button = customtkinter.CTkButton(master=self.menu_frame, text='Search',
                                                width=30, height=27, corner_radius=5,
                                                font=customtkinter.CTkFont('Sans', 13),
                                                hover_color=('gray70', 'gray30'),
                                                fg_color='gray15', image=search_image,
                                                compound='left',
                                                border_color='gray40',border_width=1,)
        search_button.place(x=650, y=20, anchor='e')
        ToolTip(search_button, msg='Search', delay=0)


        # self.dash.mainloop()


    def dashexit(self):
        if messagebox.askyesno('Logout', 'Please remember to save\nyour works\nDo you want to exit', icon='warning'):
            homepage.Homepage(self.dash)
            self.dash.destroy()
            sys.exit()
        else:
            self.dash = self.dash








if __name__ == "__main__":
    app = Dashboard()
    
    

    
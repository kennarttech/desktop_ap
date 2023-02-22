import json
import os, sys
import homepage
from tkinter import *
import customtkinter
from PIL import Image
from tkinter import ttk
from tkinter import Menu
from tkcalendar import *
from tktooltip import ToolTip
from tkinter import messagebox
from ttkthemes import themed_tk as tk




class Dashboard(customtkinter.CTkToplevel):

    customtkinter.set_appearance_mode('system')
    customtkinter.set_default_color_theme('green')


    """Using context manager to open the a json file"""
    with open(file='app/config/settings.json', mode='r') as settings_rf:
        user_data = json.load(settings_rf)


    def __init__(self) -> None:
        self.dash = customtkinter.CTk()
        # self.dash = customtkinter.CTkToplevel()
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
                                                   text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"), 
                                                   height=25, width=30,fg_color='transparent',
                                                   corner_radius=4, border_width=1,
                                                   image=daily_sales, anchor='w')
        daily_sales_button.grid(row=3, column=0, padx=10, pady=0, sticky=EW)
        ToolTip(daily_sales_button, msg='New daily sales', fg='white', bg='gray15', delay=0)



        exit_button = customtkinter.CTkButton(master=left_frame, text='  Exit/Logout',
                                                   text_color=("white"), 
                                                   fg_color=self.user_data['theme'],
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
        middle_frame.grid_rowconfigure((1,2,3,4,5,6,7), weight=1)


        
        top_frame = customtkinter.CTkFrame(master=middle_frame, border_color='gray50', 
                                           border_width=1, width=400, height=40,
                                           fg_color='gray35', corner_radius=7)
        top_frame.grid(row=0, column=0, columnspan=4, padx=(2,2), pady=(0, 0), ipady=3, sticky='ew')
        top_frame.grid_columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)


        
        item_combo = customtkinter.CTkComboBox(master=top_frame, width=150, height=30,
                                               values=['Local A4', 'Local A3', 'Foreign A3',
                                                       'Foreign A5', 'Foreign A4', 'Arwork A3',
                                                       'Artwork A2', 'Artwork A4', 'Canvas A3',
                                                       'Canvas A3', 'Canvas A2', 'Canvas A4'],
                                               corner_radius=11, border_width=2, border_color='gray50',
                                               button_color='gray50', fg_color='gray25',
                                               button_hover_color=('gray70', 'gray30'), 
                                               dropdown_fg_color='gray35', justify='left')
        item_combo.grid(row=0, column=0, padx=(0, 0), pady=(3, 0))
        item_combo.set('Item Sold')



        quantity_combo = customtkinter.CTkComboBox(master=top_frame, width=150, height=30,
                                               values=['0','1','2','3','4','5','6','7','8','9','10'],
                                               corner_radius=11, border_width=2, border_color='gray50',
                                               button_color='gray50', fg_color='gray25',
                                               button_hover_color=('gray70', 'gray30'), 
                                               dropdown_fg_color='gray35', justify='left')
        quantity_combo.grid(row=0, column=1, padx=(0, 0), pady=(3, 0))
        quantity_combo.set('Quantity')



        amount_combo = customtkinter.CTkComboBox(master=top_frame, width=150, height=30,
                                               values=['45','50','70','80','120','200','180','65','100','85'],
                                               corner_radius=11, border_width=2, border_color='gray50',
                                               button_color='gray50', fg_color='gray25',
                                               button_hover_color=('gray70', 'gray30'), 
                                               dropdown_fg_color='gray35', justify='left')
        amount_combo.grid(row=0, column=2, padx=(0, 0), pady=(3, 0))



        deposit_amount = customtkinter.CTkEntry(master=top_frame, height=30,
                                               placeholder_text='Deposit amount',
                                                width=110, corner_radius=9)
        deposit_amount.grid(row=0, column=3, padx=(0, 0), pady=(3, 0))



        deposit_name = customtkinter.CTkEntry(master=top_frame, height=30,
                                               placeholder_text='Deposit name',
                                                width=120, corner_radius=9)
        deposit_name.grid(row=0, column=4, padx=(0, 0), pady=(3, 0))



        balance = customtkinter.CTkEntry(master=top_frame, height=30,
                                               placeholder_text='Balance left',
                                                width=100, corner_radius=9)
        balance.grid(row=0, column=5, padx=(0, 0), pady=(3, 0))



        date_ = DateEntry(master=top_frame, height=58, width=10)
        date_.grid(row=0, column=6, padx=(0,0), pady=(3, 0))



        total = customtkinter.CTkEntry(master=top_frame, height=30,
                                               placeholder_text='Total amount',
                                                width=100, corner_radius=9)
        total.grid(row=0, column=7, padx=(0, 0), pady=(3, 0))



        submit_button = customtkinter.CTkButton(master=middle_frame, text='Submit Record',
                                                   text_color=("white"), 
                                                   fg_color=self.user_data['theme'],
                                                   hover_color=("gray70", "gray30"), 
                                                   height=25, width=100, anchor='S',
                                                   corner_radius=4, border_width=1,
                                                   font=('Roboto', 18),
                                                   command=None)
        submit_button.grid(row=7, column=3, padx=(30, 10), pady=(140, 10), sticky='e')
        ToolTip(submit_button, msg='Submit Record', fg='white', bg='gray15', delay=0)



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
                                            width=220, corner_radius=9)
        search_box.place(x=560, y=20, anchor='e')
        ToolTip(search_box, msg='Search for anything', delay=0)

        
        
        search_button = customtkinter.CTkButton(master=self.menu_frame, text='Search',
                                                width=30, height=27, corner_radius=8,
                                                font=customtkinter.CTkFont('Sans', 13),
                                                hover_color=('gray70', 'gray30'),
                                                fg_color='gray15', image=search_image,
                                                compound='left',
                                                border_color='gray40',border_width=1,)
        search_button.place(x=660, y=20, anchor='e')
        ToolTip(search_button, msg='Search', delay=0)



        self.dash.mainloop()


    def dashexit(self)-> None:
        if messagebox.askyesno('Logout', 'Please remember to save\nyour works\nDo you want to exit', icon='warning'):
            homepage.Homepage(self.dash)
            self.dash.destroy()
            sys.exit()
        else:
            self.dash = self.dash








if __name__ == "__main__":
    app = Dashboard()
    
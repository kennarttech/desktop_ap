"""This are built-in modules, which are part of the Python Standard Library"""
import os
import json
import requests
from tkinter import *
from tkinter import Menu


"""this are third-party modules that need to be installed separately using pip"""
import customtkinter
from PIL import Image
from tkcalendar import *
from tktooltip import ToolTip
from CTkMessagebox import CTkMessagebox


"""The are local modules that I have created myself and are part of the project. """
import newframes
from custommessage import CKTMessagebox


class Dashboard(customtkinter.CTkToplevel):


    customtkinter.set_appearance_mode('system')
    customtkinter.set_default_color_theme('green')


    """Using context manager to open the a json file"""
    with open(file='app/config/settings.json', mode='r') as _rf:
        user_data = json.load(_rf)


    def __init__(self) -> None:
        # self.dash = customtkinter.CTk()
        self.dash = customtkinter.CTkToplevel()
        self.dash.minsize(900, 500)
        self.dash.attributes('-zoomed', True)
        self.dash.geometry('1000x600+155+50')
        self.dash.title('Welcome to DS Enterprise')


        self.icon_image = PhotoImage(file='app/icons/logo_03.png')
        self.dash.tk.call('wm', 'iconphoto', self.dash._w, self.icon_image)


        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'icons')
        user_profile_logo = customtkinter.CTkImage(Image.open(os.path.join(image_path,
                                                                           'logo_12.png')), 
        size=(130, 130))


        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'icons')
        new_frames = customtkinter.CTkImage(Image.open(os.path.join(image_path,
                                                                    'logo_10.png')),
        size=(30, 30))


        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'icons')
        daily_sales = customtkinter.CTkImage(Image.open(os.path.join(image_path,
                                                                     'logo_14.png')),
        size=(30, 30))


        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'icons')
        back_home = customtkinter.CTkImage(Image.open(os.path.join(image_path, 
                                                                   'logo_07.png')), 
        size=(30, 30))


        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'icons')
        search_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, 
                                                                      'logo_08.png')), 
        size=(22, 22))


        self.dash.columnconfigure((1,2), weight=1, uniform='a')
        self.dash.rowconfigure(0, weight=1, uniform='a')


        self.menu = Menu(self.dash)
        self.dash.config(menu = self.menu)
        self.filename = Menu(self.menu, tearoff=0, activebackground=self.user_data
                             ['menu_background_color'], activeforeground='white')
        self.menu.add_cascade(label='File', menu = self.filename)
        self.filename.add_command(label = 'Save', accelerator = 'Ctrl+S', command=None)
        self.filename.add_separator()
        self.filename.add_command(label = 'Exit', image = None, compound = LEFT, 
                                  accelerator = 'Ctrl+E', command = self.usr_exit)


        self.help = Menu(self.menu, tearoff=0, activebackground=self.user_data
                         ['menu_background_color'], activeforeground='white')
        self.menu.add_cascade(label = "Help", menu = self.help)
        self.help.add_command(label = 'About ', accelerator="Ctrl+A", command=None)


        self.option_menu = Menu(self.menu, tearoff=0, activebackground=self.user_data
                                ['menu_background_color'], activeforeground='white')
        self.menu.add_cascade(label = "Options", menu = self.option_menu)
        self.option_menu.add_command(label = 'Print', accelerator='Ctrl+P', command=None)
        self.option_menu.add_command(label = 'View All Data', 
                                     accelerator='Ctrl+I', command=None)
        self.option_menu.add_command(label = 'Modify Saved Data', accelerator='Ctrl+M',
                                     command=None)
        

        left_frame = customtkinter.CTkFrame(master=self.dash, 
                                            border_color='gray10', 
                                            border_width=0.8,
                                            fg_color='#06283D',
                                            corner_radius=5)
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
                                                   height=25, width=30, anchor='w',
                                                   corner_radius=5, border_width=1,
                                                   image=new_frames, command=self.gotonewf)
        new_frame_button.grid(row=2, column=0, padx=10, pady=2, sticky=EW)
        ToolTip(new_frame_button, msg='Upload new frames', fg='white', bg='gray15', delay=0)


        daily_sales_button = customtkinter.CTkButton(master=left_frame, text='Daily Sales',
                                                   text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"), 
                                                   height=25, width=30, border_width=1,fg_color='transparent',
                                                   corner_radius=5, anchor='w',
                                                   image=daily_sales, command=self.nothing)
        daily_sales_button.grid(row=3, column=0, padx=10, pady=0, sticky=EW)
        ToolTip(daily_sales_button, msg='New daily sales', fg='white', bg='gray15', delay=0)


        exit_button = customtkinter.CTkButton(master=left_frame, text='  Exit/Logout',
                                                   text_color=("white"), 
                                                   fg_color=self.user_data['theme'],
                                                   hover_color=("gray70", "gray30"), 
                                                   height=25, width=100, anchor='S',
                                                   corner_radius=5, border_width=1,
                                                   font=('Roboto', 14),image=back_home,
                                                   command=self.usr_exit)
        exit_button.grid(row=4,  padx=1, pady=50, sticky='s')
        ToolTip(exit_button, msg='Exit the program', fg='white', bg='gray15', delay=0)


        """This column downwards defines top, middle and down frames"""
        self.menu_frame = customtkinter.CTkFrame(master=self.dash, border_width=0.6,
                                           border_color='gray10', fg_color='#06283D',
                                           corner_radius=5, width=1200, height=40)
        self.menu_frame.grid(row=0, column=1, columnspan=2, padx=(20,20), pady=(0, 12), sticky=N)
        self.menu_frame.grid_columnconfigure((0,1,2,3), weight=1)
        

        middle_frame = customtkinter.CTkFrame(master=self.dash, border_width=0.6,
                                           border_color='gray10', fg_color='#2C3333',
                                           corner_radius=5, width=1200, height=100)
        middle_frame.grid(row=0, column=1, columnspan=2, padx=(20,20), pady=(60, 60), sticky=NSEW)
        middle_frame.grid_columnconfigure((0,1,2,3), weight=1)
        middle_frame.grid_rowconfigure((1,2,3,4,5,6,7), weight=1)

        
        top_frame = customtkinter.CTkFrame(master=middle_frame, border_color='gray50', 
                                           border_width=1, width=400, height=40,
                                           fg_color='gray28', corner_radius=7)
        top_frame.grid(row=0, column=0, columnspan=4, padx=(2,2), pady=(0, 0), ipady=3, sticky='ew')
        top_frame.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)

        
        item_combo = customtkinter.CTkComboBox(master=top_frame, width=150, height=30,
                                               values=['Local A4', 'Local A3', 'Foreign A3',
                                                       'Foreign A5', 'Foreign A4', 'Arwork   A3', 
                                                       'Artwork A2', 'Artwork A4', 
                                                       'Canvas A3', 'Canvas A3', 'Canvas A2',
                                                        'Canvas A4', "Mug"],
                                               corner_radius=11, border_width=2, border_color='gray50',
                                               button_color='gray50', fg_color='gray25',
                                               button_hover_color=('gray70', 'gray30'), 
                                               dropdown_fg_color='gray35', justify='left')
        item_combo.grid(row=0, column=0, padx=(0, 0), pady=(3, 0))
        item_combo.set('Item Sold')
        ToolTip(item_combo, msg='Select frames', fg='white', bg='gray15', delay=0)


        item_quantity = customtkinter.CTkComboBox(master=top_frame, width=120, height=30,
                                               values=['0','1','2','3','4','5',
                                                       '6','7','8','9','10'],
                                               corner_radius=11, border_width=2, border_color='gray50',
                                               button_color='gray50', fg_color='gray25',
                                               button_hover_color=('gray70', 'gray30'), 
                                               dropdown_fg_color='gray35', justify='left')
        item_quantity.grid(row=0, column=1, padx=(0, 0), pady=(3, 0))
        item_quantity.set('Quantity')


        item_price = customtkinter.CTkComboBox(master=top_frame, width=100, height=30,
                                               values=self.user_data["Item_prices"],
                                               corner_radius=11, border_width=2, border_color='gray50',
                                               button_color='gray50', fg_color='gray25',
                                               button_hover_color=('gray70', 'gray30'), 
                                               dropdown_fg_color='gray35', justify='left')
        item_price.grid(row=0, column=2, padx=(0, 0), pady=(3, 0))
        item_price.set('price')


        deposit_amount = customtkinter.CTkEntry(master=top_frame, height=30,
                                               placeholder_text='Deposit amount',
                                                width=110, corner_radius=9)
        deposit_amount.grid(row=0, column=3, padx=(0, 0), pady=(3, 0))


        deposit_name = customtkinter.CTkEntry(master=top_frame, height=30,
                                               placeholder_text='Deposit name',
                                                width=120, corner_radius=9)
        deposit_name.grid(row=0, column=4, padx=(0, 0), pady=(3, 0))


        deposit_contact = customtkinter.CTkEntry(master=top_frame, height=30,
                                               placeholder_text='Contact',
                                                width=120, corner_radius=9)
        deposit_contact.grid(row=0, column=5, padx=(0, 0), pady=(3, 0))


        balance = customtkinter.CTkEntry(master=top_frame, height=30,
                                               placeholder_text='Balance left',
                                                width=100, corner_radius=9)
        balance.grid(row=0, column=6, padx=(0, 0), pady=(3, 0))
        ToolTip(balance, msg='Deposit balance', fg='white', bg='gray15', delay=0)


        date_ = DateEntry(master=top_frame, height=58, width=10, justify='center')
        date_.grid(row=0, column=7, padx=(0,0), pady=(3, 0))
        ToolTip(date_, msg="Today's date", fg='white', bg='gray15', delay=0)


        total = customtkinter.CTkEntry(master=top_frame, height=30,
                                               placeholder_text='Total cost',
                                                width=100, corner_radius=9)
        total.grid(row=0, column=8, padx=(0, 0), pady=(3, 0))
        ToolTip(total, msg='Total cost', fg='white', bg='gray15', delay=0)


        # display_records = customtkinter.CTkLabel(master=middle_frame, 
        #                                          text='Nothing to display yet.....', 
        #                                          font=('Sans', 12))
        # display_records.grid(row=9, column=2, padx=(5, 0), pady=(2, 2))


        # response = requests.get('http://127.0.0.1:4000/store', json={'store': self.stores})


        print_data = customtkinter.CTkButton(master=middle_frame, text='Print Data',
                                                   text_color=("white"), 
                                                   fg_color=self.user_data['theme3'],
                                                   hover_color=("gray70", "gray30"), 
                                                   height=30, width=106, anchor='S',
                                                   corner_radius=4, border_width=1,
                                                   font=('Roboto', 16),command=None)
        print_data.grid(row=7, column=3, padx=(0, 130), pady=(140, 10), sticky='e')


        submit_button = customtkinter.CTkButton(master=middle_frame, text='Save Record',
                                                   text_color=("white"), 
                                                   fg_color=self.user_data['theme2'],
                                                   hover_color=("gray70", "gray30"), 
                                                   height=30, width=106, anchor='S',
                                                   corner_radius=4, border_width=1,
                                                   font=('Roboto', 16),command=None)
        submit_button.grid(row=7, column=3, padx=(30, 10), pady=(140, 10), sticky='e')


        buttom_frame = customtkinter.CTkFrame(master=self.dash, border_width=0.6,
                                              border_color='gray10', fg_color='#06283D',
                                              corner_radius=4, width=1200, height=25)
        buttom_frame.grid(row=0, column=1, columnspan=5, pady=(0, 0), sticky=S)
        buttom_frame.grid_columnconfigure((0,1,2,3), weight=1)
        """End of the frames"""


        menu_frame_label = customtkinter.CTkLabel(master=self.menu_frame, 
                                                  text='Daily Sales',
                                                  text_color='#16FF00', 
                                                  font=('Sans', 15),)
        menu_frame_label.place(x=40, y=20, anchor='w')


        search_box = customtkinter.CTkEntry(master=self.menu_frame, 
                                            placeholder_text='Search for deposite/name.....',
                                            width=220, corner_radius=9)
        search_box.place(x=560, y=20, anchor='e')
        ToolTip(search_box, msg='Search for record', delay=0)

        
        search_button = customtkinter.CTkButton(master=self.menu_frame, text='Search',
                                                width=30, height=27, corner_radius=8,
                                                font=customtkinter.CTkFont('Sans', 13),
                                                hover_color=('gray70', 'gray30'),
                                                fg_color='gray15', image=search_image,
                                                compound='left',
                                                border_color='gray40',border_width=1,)
        search_button.place(x=660, y=20, anchor='e')
        ToolTip(search_button, msg='Search', delay=0)


        """This code takes tuple from a user as in 'Shortcut' to perform task"""
        # self.dash.bind('<Control-a>', self.about)
        # self.dash.bind('<Control-A>', self.about)
        self.dash.bind('<Control-E>', self.usr_exit)
        self.dash.bind('<Control-e>', self.usr_exit)


        # self.dash.mainloop()


    def usr_exit(self, *event)-> None:
        CKTMessagebox(self.dash)


    def gotonewf(self):
        msg = CTkMessagebox(title="Logout", message="Do you want to switch to New-Record?",
                        icon="info", 
                        option_1="Yes", 
                        option_2="No")
        response = msg.get()
        if response == 'Yes':
            newframes.Newframe()
            self.dash.destroy()
        else:
            self.dash = self.dash


    def nothing(self):
        if CTkMessagebox(title='Dashboard', message='Option not available yet', 
                         icon='info'):
            return self.dash



if __name__ == "__main__":
    app = Dashboard()
    
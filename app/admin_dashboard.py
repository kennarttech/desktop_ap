"""This are built-in modules, which are part of the Python Standard Library"""
import os
import json
import sched
from tkinter import *
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox


"""this are third-party modules that need to be installed separately using pip"""
import customtkinter
from PIL import Image
from tkcalendar import *
from tktooltip import ToolTip


"""This are local modules that I have created myself and are part of the project. """
import newframes
import dashboard
import about
import customnote
from custommessage import Closewindowdhboard


class Adminsuper(customtkinter.CTkToplevel):
    """This class defines the Admin page, which is use create the GUI"""


    default = customtkinter.set_appearance_mode('system')
    custom = customtkinter.set_default_color_theme('green')


    """Using context manager to open the a json file"""
    with open(file='app/config/settings.json', mode='r') as _rf:
        user_data = json.load(_rf)


    def __init__(self) -> None:
        # self.admin__a = customtkinter.CTk()
        self.admin__a = customtkinter.CTkToplevel()
        self.admin__a.minsize(400, 430)
        self.admin__a.attributes('-zoomed', True)
        self.admin__a.geometry('1000x600+155+50')
        self.admin__a.title('Welcome to DS Enterprise')


        self.icon_image = PhotoImage(file='app/icons/logo_03.png')
        self.admin__a.tk.call('wm', 'iconphoto', self.admin__a._w, self.icon_image)


        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'icons')
        user_profile_logo = customtkinter.CTkImage(Image.open(os.path.join(image_path,'logo_05.png')), 
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


        self.admin__a.columnconfigure((1,2), weight=1, uniform='a')
        self.admin__a.rowconfigure(0, weight=1, uniform='a')


        self.menu = Menu(self.admin__a)
        self.admin__a.config(menu = self.menu)
        self.filename = Menu(self.menu, tearoff=0, 
                             activebackground=self.user_data['admin_color2'])
        self.menu.add_cascade(label='File', menu=self.filename)
        self.filename.add_command(label='Save       ', accelerator='Ctrl+S', command=None)
        self.filename.add_separator()
        self.filename.add_command(label='Exit       ', image=None, compound=LEFT, 
                                  accelerator='Ctrl+E', command=self.admin__aexit)


        self.help = Menu(self.menu, tearoff=0, 
                         activebackground=self.user_data['admin_color2'], activeborderwidth=0)
        self.menu.add_cascade(label='Help', menu = self.help)
        self.help.add_command(label='About      ', accelerator='Ctrl+A', command=self.about)


        self.option_menu = Menu(self.menu, tearoff=0, 
                                activebackground=self.user_data['admin_color2'])
        self.menu.add_cascade(label='Options', menu = self.option_menu)
        self.option_menu.add_command(label='Print       ', accelerator='Ctrl+P', command=None)
        self.option_menu.add_command(label='View All Data', accelerator='Ctrl+I', command=None)


        left_frame = customtkinter.CTkFrame(master=self.admin__a, 
                                            border_color='gray10', 
                                            border_width=0.8,
                                            fg_color=self.user_data['admin_color2'], 
                                            corner_radius=8)
        left_frame.grid(row=0, column=0, padx=(10,0), ipadx=(10), pady=(10, 20), sticky=NSEW)
        left_frame.grid_rowconfigure((0,1,2,3,4,5), weight=1)


        user_profile = customtkinter.CTkLabel(master=left_frame, text='',
                                              image=user_profile_logo,
                                              font=customtkinter.CTkFont('Roboto', 18),
                                              text_color='gray12')
        user_profile.grid(row=0, column=0, padx=20, pady=1, sticky=NSEW)


        new_frame_button = customtkinter.CTkButton(master=left_frame, text='New Frames',
                                                   text_color=("gray10", "gray90"), fg_color='transparent',
                                                   hover_color=("gray70", "gray30"), 
                                                   height=25, width=30, anchor='w',
                                                   corner_radius=6, border_width=1,
                                                   image=new_frames, command=self.gotonewf)
        new_frame_button.grid(row=2, column=0, padx=10, pady=2, sticky=EW)
        ToolTip(new_frame_button, msg='Upload new frames', fg='white', bg='gray15', delay=0)


        daily_sales_button = customtkinter.CTkButton(master=left_frame, height=25,  
                                                    text='User dashboard',
                                                   text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"), 
                                                   border_width=1,fg_color='transparent',
                                                   corner_radius=6, anchor='w', width=30,
                                                   image=daily_sales, command=self.usrnothing)
        daily_sales_button.grid(row=3, column=0, padx=10, pady=0, sticky=EW)
        ToolTip(daily_sales_button, msg='Users dashboard', fg='white', bg='gray15', delay=0)


        exit_button = customtkinter.CTkButton(master=left_frame, text='  Exit/Logout',
                                                   text_color=("white"), 
                                                   fg_color=self.user_data['theme4'],
                                                   hover_color=("gray70", "gray30"), 
                                                   height=25, width=100, anchor='S',
                                                   corner_radius=6, border_width=1,
                                                   font=('Roboto', 14),image=back_home,
                                                   command=self.admin__aexit)
        exit_button.grid(row=4,  padx=1, pady=50, sticky='s')
        ToolTip(exit_button, msg='Exit the program', fg='white', bg='gray15', delay=0)


        """This column downwards defines top, middle and down frames"""
        self.menu_frame = customtkinter.CTkFrame(master=self.admin__a, border_width=0.6,
                                           border_color='gray10', fg_color=self.user_data['admin_color2'],
                                           corner_radius=5, width=1200, height=40)
        self.menu_frame.grid(row=0, column=1, columnspan=2, padx=(19,19), pady=(10, 12), sticky=N)
        self.menu_frame.grid_columnconfigure((0,1,2,3), weight=1)


        middle_frame = customtkinter.CTkFrame(master=self.admin__a, border_width=1,
                                           border_color='gray40', fg_color=self.user_data['admin_color3'],
                                           corner_radius=5, width=1200, height=100)
        middle_frame.grid(row=0, column=1, columnspan=2, padx=(20,20), pady=(57, 60), sticky=NSEW)
        middle_frame.grid_columnconfigure((0,1,2,3), weight=1)
        middle_frame.grid_rowconfigure((1,2,3,4,5,6,7), weight=1)

        
        top_frame = customtkinter.CTkFrame(master=middle_frame, border_color='gray50', 
                                           border_width=0.6, width=400, height=40,
                                           fg_color=self.user_data['admin_color2'], corner_radius=5)
        top_frame.grid(row=0, column=0, columnspan=4, padx=(2,2), pady=(0, 0), ipady=3, sticky='ew')
        top_frame.grid_columnconfigure((0,1,2,3,4,5,6,7,8,10,12), weight=1)


        admin_sales = customtkinter.CTkEntry(master=top_frame, height=30,
                                               placeholder_text='Daily Sales',
                                                width=120, corner_radius=9)
        admin_sales.grid(row=0, column=0, padx=(0, 0), pady=(3, 0))
        ToolTip(admin_sales, msg='daily sales', fg='white', bg='gray15', delay=0)


        daily_expenses = customtkinter.CTkEntry(master=top_frame, height=30,
                                               placeholder_text='Daily Expenses',
                                                width=120, corner_radius=9)
        daily_expenses.grid(row=0, column=2, padx=(0, 0), pady=(3, 0))
        ToolTip(daily_expenses, msg='daily expenses', fg='white', bg='gray15', delay=0)


        txt_note = customtkinter.CTkButton(master=top_frame, width=100, text='New Note',
                                             height=29, fg_color=('gray15'), 
                                             font=('Sans', 13), 
                                             hover_color=('gray70', 'gray30'),
                                             corner_radius=8, command=self.adminnote)
        txt_note.grid(row=0, column=4, padx=(0,0), pady=(4,0))


        date_ = DateEntry(master=top_frame, height=58, width=10, justify='center')
        date_.grid(row=0, column=6, padx=(0,0), pady=(3, 0))
        ToolTip(date_, msg='Todays date', fg='white', bg='gray15', delay=0)


        total = customtkinter.CTkEntry(master=top_frame, height=30,
                                               placeholder_text='Total sales',
                                                width=100, corner_radius=9)
        total.grid(row=0, column=12, padx=(0, 0), pady=(3, 0))
        ToolTip(total, msg='Total sales', fg='white', bg='gray15', delay=0)


        display_records = customtkinter.CTkLabel(master=middle_frame, 
                                                 text='Nothing to display yet.....', 
                                                 font=('Sans', 12))
        display_records.grid(row=5, column=2, padx=(5, 0), pady=(2, 2))


        print_data = customtkinter.CTkButton(master=middle_frame, text='Print Data',
                                                   text_color=("white"), 
                                                   fg_color=self.user_data['theme3'],
                                                   hover_color=("gray70", "gray30"), 
                                                   height=30, width=106, anchor='S',
                                                   corner_radius=4, border_width=1,
                                                   font=('Roboto', 16),command=None)
        print_data.grid(row=7, column=3, padx=(0, 130), pady=(140, 10), sticky='e')
        ToolTip(print_data, msg='Print Record', fg='white', bg='gray15', delay=0)


        submit_button = customtkinter.CTkButton(master=middle_frame, text='Save Record',
                                                   text_color=("white"), 
                                                   fg_color=self.user_data['theme2'],
                                                   hover_color=("gray70", "gray30"), 
                                                   height=30, width=106, anchor='S',
                                                   corner_radius=4, border_width=1,
                                                   font=('Roboto', 16),command=None)
        submit_button.grid(row=7, column=3, padx=(30, 10), pady=(140, 10), sticky='e')
        ToolTip(submit_button, msg='Submit Record', fg='white', bg='gray15', delay=0)


        buttom_frame = customtkinter.CTkFrame(master=self.admin__a, border_width=0.6,
                                              border_color='gray10', fg_color=self.user_data['admin_color2'],
                                              corner_radius=4, width=1200, height=30)
        buttom_frame.grid(row=0, column=1, columnspan=5, padx=(19, 19), pady=(0, 20), sticky=S)
        buttom_frame.grid_columnconfigure((0,1,2,3), weight=1)
        """End of the frames"""


        menu_frame_label = customtkinter.CTkLabel(master=self.menu_frame, 
                                                  text=self.user_data['master'],
                                                  text_color=self.user_data['admin_color'], 
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
        self.admin__a.bind('<Control-a>', self.about)
        self.admin__a.bind('<Control-A>', self.about)
        self.admin__a.bind('<Control-E>', self.admin__aexit)
        self.admin__a.bind('<Control-e>', self.admin__aexit)


        # self.admin__a.mainloop()


    def about(self, *args):
        about.Aboutpage()


    def admin__aexit(self, *event)-> None:
        Closewindowdhboard(self.admin__a)
    

    def adminnote(self):
        customnote.CustomNote(self.admin__a)


    def gotonewf(self):
        if messagebox.askyesno('New frame', 'Welcome to users dashboard\nDo you want to proceed', icon='info'):
            newframes.Newframe()
            self.admin__a.destroy()
        else:
            self.admin__a = self.admin__a


    def usrnothing(self):
        if messagebox.askyesno('admin__abord', 'Users page', icon='info'):
            dashboard.Dashboard()
            self.admin__a.destroy()
        else:
            self.admin__a = self.admin__a



if __name__ == "__main__":
    app = Adminsuper()
    
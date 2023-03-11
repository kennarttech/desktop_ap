"""This are built-in modules, which are part of the Python Standard Library"""
import os
import json
from tkinter import *
from PIL import Image
from tktooltip import ToolTip


"""this are third-party modules that need to be installed separately using pip"""
import customtkinter


class EditData(customtkinter.CTkToplevel):
    """This class defines the data_editpage, that is use create the GUI"""
    customtkinter.set_appearance_mode('system')


    """Using contex manager to open txt file for reading mode"""
    TEXT_FILE_PATH = "app/config/about.json"

    with open(file=TEXT_FILE_PATH, mode='r', encoding='utf-8') as rf:
        user_data = json.load(rf)


    def __init__(self) -> None:
        # self.data_edit = customtkinter.CTk()
        self.data_edit = customtkinter.CTkToplevel()
        self.data_edit.title('Modify Data')
        self.data_edit.resizable(0, 0)
        self.data_edit.geometry('720x450+365+130')
        icon_image = PhotoImage(file='app/icons/logo_04.png')
        self.data_edit.tk.call('wm', 'iconphoto', self.data_edit._w, icon_image)
      

        self.data_edit.columnconfigure(0, weight=1, uniform='a')
        self.data_edit.rowconfigure((1, 2), weight = 1, uniform='a')


        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 
                                  'icons')
        search_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, 
                                                                      'logo_08.png')), 
        size=(22, 22))


        top_frame = customtkinter.CTkFrame(self.data_edit, 
                                            border_width = 0.7, 
                                            border_color ='gray20',
                                            corner_radius = 3,
                                            height=35)
        top_frame.grid(row = 0, column = 0, ipady=3, sticky = NSEW)
        top_frame.grid_columnconfigure((1, 2), weight = 1)


        top_frame_label = customtkinter.CTkLabel(master=top_frame, 
                                                text='Enter record ID =>>', 
                                                font=('TImes', 22))
        top_frame_label.grid(row=0, column=0, padx=(18, 0), pady=(7, 0))


        search_box = customtkinter.CTkEntry(master=top_frame, 
                                            placeholder_text=self.user_data
                                            ['entry_search'],
                                            width=230, corner_radius=10)
        search_box.grid(row=0, column=1, padx=(40, 0), pady=(6, 0))
        ToolTip(search_box, msg='Search for record', delay=0)
        search_box.focus()

        
        search_button = customtkinter.CTkButton(master=top_frame, text='Search',
                                                width=30, height=27, corner_radius=8,
                                                font=customtkinter.CTkFont('Sans', 13),
                                                hover_color=('gray70', 'gray30'),
                                                fg_color='gray15', image=search_image,
                                                compound='left',
                                                border_color='gray40',border_width=1,)
        search_button.grid(row=0, column=2, padx=(0, 80), pady=(6, 0))
        ToolTip(search_button, msg='Search', delay=0)


        # self.data_edit.mainloop()


    """This method exit the data_edit window when the button is press"""
    def data_editexit(self) -> None:
        pass
        # homepage.Homepage(self.data_edit)
        # self.data_edit.destroy()



if __name__ == "__main__":
    """this returns True if the script is run directly else it return False"""
    app = EditData()
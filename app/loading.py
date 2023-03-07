import os
import customtkinter
from tkinter import *
from PIL import Image


WIDTH: int=540
HEIGHT: int=400


main_window = customtkinter.CTk()
main_window.resizable(0, 0)
main_window.minsize(500, 400)
main_window.title('Loading Page')
main_window.attributes('-alpha', 0.7)
customtkinter.set_appearance_mode('#241f31')
main_window.geometry(f'{WIDTH}x{HEIGHT}+416+165')


"""This script is use to set windows icons"""
icon_image = PhotoImage(file='app/icons/logo_03.png')
main_window.tk.call('wm', 'iconphoto', main_window._w, icon_image)


"""This script returns the path of the icons"""
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 
                          "icons")
logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, 
                                                            "logo_05.png")), 
size=(300,300))


"""This script is use to configure the main_window"""
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=0)
main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=0)


progress_logo = customtkinter.CTkLabel(master=main_window, 
                                       text="", image=logo_image)
progress_logo.grid(row=0, column=0, padx=20, pady=20)


progress_label = customtkinter.CTkLabel(master = main_window, text = '', 
                                        font = ('Sans', 16))
progress_label.grid(row=1, column=0,  sticky=NSEW)


progress_bar = customtkinter.CTkProgressBar(master = main_window, 
                                            width = 480, 
                                            height = 15, mode='determinate', 
                                            corner_radius=7,
                                            orientation='horizontal', 
                                            determinate_speed= 2,
                                            border_width=1, 
                                            progress_color='#16FF00')
progress_bar.grid(row=2, column=0, padx=20, pady=20, sticky=EW)
progress_bar.set(0.0)


def user_homepage()-> None:
    """This function call user_homepage after ProgressBar finish loading"""
    main_window.withdraw()
    os.system("python app/homepage.py")
    main_window.destroy()


counter = 0
def loading_progress_bar(value) -> str:
    """This function loads the page!! Refer to (README2.md in the package folder) """
    progress_bar.set(value)
    global counter
    if counter <= 10:
        test = 'Please wait, While we load your homepage ....⌛ [' + \
        (str(10 * counter) + '%]')
        progress_label.configure(text=test)
        progress_bar.after(1000, loading_progress_bar, value + 1/10)
        counter += 1
    else:
        user_homepage()

loading_progress_bar(0)


main_window.mainloop()
import os
import customtkinter
from tkinter import *
from tkinter import ttk





WIDTH: int=1366
HEIGHT: int=768
WIDTH: int=540
HEIGHT: int=400

customtkinter.set_appearance_mode('dark')


window = customtkinter.CTk()
window.resizable(0, 0)
window.minsize(500, 400)
window.title('Loading Progress')
window.geometry(f'{WIDTH}x{HEIGHT}+{416}+{165}')
img = PhotoImage(file='app/icons/AA.png')
window.tk.call('wm', 'iconphoto', window._w, img)


"""This script is use to configure the window"""
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=0)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=0)



label = customtkinter.CTkLabel(master=window, text = 'Welcome To DS Enterprise', 
                                font=('Times', 22), )
label.grid(row=0, column=0, ipady=30, ipadx=30, sticky=N)


progress_label = customtkinter.CTkLabel(master = window, text = 'Please Wait....', 
                                font = ('Roboto', 18))
progress_label.grid(row=1, column=0,  sticky=NSEW)


progress = customtkinter.CTkProgressBar(master = window, width = 480, 
                                    height = 18, mode='determinate', 
                                    orientation='horizontal', determinate_speed= 2,
                                    border_width=1, progress_color='#16CF13')
progress.grid(row=2, column=0, padx=20, pady=20, sticky=EW)
progress.set(0.0)



def user_login():
    """This function defines user login page after ProgressBar finish loading"""
    window.withdraw()
    os.system("python app/login.py")
    window.destroy()



counter = 0
def loading_progress_bar(value):
    """This function loads the page!! Refere to (README2.md) """
    progress.set(value)
    global counter
    if counter <= 10:
        test = 'Please Wait.... ' + (str(10 * counter) + '%')
        progress_label.configure(text=test)
        progress.after(1000, loading_progress_bar, value + 1/10)
        counter += 1
    else:
        user_login()

loading_progress_bar(0)






window.mainloop()
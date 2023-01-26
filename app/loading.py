import os
import customtkinter
from tkinter import *
from tkinter import ttk





WIDTH: int=1366
HEIGHT: int=768
WIDTH: int=540
HEIGHT: int=400


main_window = customtkinter.CTk()
main_window.resizable(0, 0)
main_window.minsize(500, 400)
main_window.title('Loading Progress')
customtkinter.set_appearance_mode('light')
main_window.geometry(f'{WIDTH}x{HEIGHT}+{416}+{165}')



icon_img = PhotoImage(file='app/icons/AA.png')
main_window.tk.call('wm', 'iconphoto', main_window._w, icon_img)


"""This script is use to configure the main_window"""
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=0)
main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=0)



label = customtkinter.CTkLabel(master=main_window, text = 'Welcome To DS Enterprise', 
                                font=('Times', 22), )
label.grid(row=0, column=0, ipady=30, ipadx=30, sticky=N)


progress_label = customtkinter.CTkLabel(master = main_window, text = 'Please Wait....', 
                                        font = ('Roboto', 18))
progress_label.grid(row=1, column=0,  sticky=NSEW)


progress_bar = customtkinter.CTkProgressBar(master = main_window, width = 480, 
                                    height = 18, mode='determinate', 
                                    orientation='horizontal', determinate_speed= 2,
                                    border_width=1, progress_color='#16CF13')
progress_bar.grid(row=2, column=0, padx=20, pady=20, sticky=EW)
progress_bar.set(0.0)



def user_homepage():
    """This function is call user user_homepage after ProgressBar finish loading"""
    main_window.withdraw()
    os.system("python app/homepage.py")
    main_window.destroy()



counter = 0
def loading_progress_bar(value):
    """This function loads the page!! Refere to (README2.md) """
    progress_bar.set(value)
    global counter
    if counter <= 10:
        test = 'Please Wait.... ' + (str(10 * counter) + '%')
        progress_label.configure(text=test)
        progress_bar.after(1000, loading_progress_bar, value + 1/10)
        counter += 1
    else:
        user_homepage()

loading_progress_bar(0)



main_window.mainloop()
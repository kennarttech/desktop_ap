import os
from tkinter import *
import customtkinter
import login
from tkinter.ttk import Progressbar


"""window.geometry(1366x768)"""
customtkinter.set_appearance_mode('dark')


window = customtkinter.CTk()
window.geometry('530x400+416+165')
window.title('Loading Progress')
img = PhotoImage(file='/home/kenneth/Desktop/desktop_ap/app/icons/AA.png')
window.tk.call('wm', 'iconphoto', window._w, img)
window.minsize(500, 400)
window.resizable(0, 0)


window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=0)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=0)


label = customtkinter.CTkLabel(master=window, text = 'Welcome to Kennart Tech', 
                                font=('Times', 22), )
label.grid(row=0, column=0, ipady=30, ipadx=30, sticky=N)


progress_label = customtkinter.CTkLabel(master = window, text = 'Please Wait....', 
                                font = ('Times', 20))
progress_label.grid(row=1, column=0,  sticky=NSEW)



progress = customtkinter.CTkProgressBar(master = window, width = 480, 
                                    height = 15, mode='determinate', 
                                    orientation='horizontal')
progress.grid(row=2, column=0, padx=20, pady=20, sticky=EW)
progress.start()



def userlogin():
    window.withdraw()
    os.system('python', 'login.py')
    window.destroy()


i = 0
def progressload():
    global i
    if i <= 10:
        txt = 'Please Wait.... ' + (str(10 * i) + '%')
        progress_label.configure(text=txt)
        progress_label.after(1000, progressload)
        progress['value'] = 10 * i
        i += 1
    else:
        userlogin()

progressload()









window.mainloop()
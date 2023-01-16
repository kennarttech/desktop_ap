from tkinter import *
import customtkinter


customtkinter.set_appearance_mode("dark")


class Loadingpage():
    def __init__(self) -> None:
        prog = customtkinter.CTk()
        prog.geometry('530x400+416+165')
        prog.title('Loading Page')
        img = PhotoImage(file='app/icons/AA.png')
        
        prog.tk.call('wm', 'iconphoto', prog._w, img)

        p1 = customtkinter.CTkProgressBar(prog, orientation=HORIZONTAL, 
                                            mode='determinate', 
                                            width=480, height=15)
        p1.place(x=25, y=360 )


        top_lable = customtkinter.CTkLabel(prog, text='Welcome to Kennart Tech',
                                            font=customtkinter.CTkFont("Times", 30))
        top_lable.place(x=80, y=20)


        prog_lable = customtkinter.CTkLabel(prog, text='Please wait.....', 
        font=customtkinter.CTkFont("Times", 25))
        prog_lable.place(x=210, y=320)


        prog.mainloop()
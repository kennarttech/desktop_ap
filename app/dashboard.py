from tkinter import *
import customtkinter



class Dashboard():
    def __init__(self) -> None:
        # self.dash = customtkinter.CTk()
        self.dash = customtkinter.CTkToplevel()
        self.dash.attributes('-zoomed', True)
        self.dash.geometry('1000x600+155+50')
        self.dash.title('Dashboard')


        self.dash.columnconfigure(0, weight=1, uniform='a')
        self.dash.rowconfigure(0, weight=0, uniform='a')
        # self.dash.mainloop()








if __name__ == "__main__":
    app = Dashboard()


from tkinter import *
from tkinter import ttk
import customtkinter

os = customtkinter.CTk()
os.geometry('400x400')



menu_frame = customtkinter.CTkFrame(os, bg_color='teal')
menu_frame.grid_columnconfigure((0,1,2,3), weight=1, uniform='a')
menu_frame.grid_rowconfigure((0,1,2,3,4), weight=1, uniform='a')


main_frame = customtkinter.CTkFrame(os)
main_frame.columnconfigure(4, weight=1)
main_frame.rowconfigure(6, weight=1)


toggle_frame = customtkinter.CTkFrame(menu_frame)
toggle_frame.grid(row=4, column=0, columnspan=4, sticky=NSEW)


menu_toggle1 = ttk.Checkbutton(toggle_frame, text='Check 2')
menu_toggle1.pack(side='right', expand=True)


entry = customtkinter.CTkEntry(main_frame)
entry.place(relx=0.10, rely=0.5, anchor=W, width=150, height=35)
entry.focus()


menu_frame.place(x=0, y=0, relwidth=0.3, relheight=1)
main_frame.place(relx=0.3, y=0, relwidth=0.7, relheight=1)


menu_button1 = customtkinter.CTkButton(menu_frame, text='Button 1')
menu_button1.grid(row=0, column=0, sticky='nswe', columnspan=2)


menu_button2 = customtkinter.CTkButton(menu_frame, text='Button 2')
menu_button2.grid(row=0, column=2, sticky='nswe')


menu_button3 = customtkinter.CTkButton(menu_frame, text='Button 3')
menu_button3.grid(row=3, column=0, sticky='nswe',columnspan=3, )






os.mainloop()









import customtkinter
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x300")
        self.title("small example app")
        self.minsize(300, 200)
        # create 2x2 grid system

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.textbox = customtkinter.CTkTextbox(master=self)
        self.textbox.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")

        self.combobox = customtkinter.CTkComboBox(master=self, values=["Sample text 1", "Text 2"])
        self.combobox.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

             
        self.button = customtkinter.CTkButton(master=self, command=self.button_callback, text="Insert Text")
        self.button.grid(row=1, column=1, padx=20, pady=20, sticky="ew")


    def button_callback(self):
        self.textbox.insert("insert", self.combobox.get() + "\n")

if __name__ == "__main__":
    app = App()
    app.mainloop()



import tkinter as tk

root = tk.Tk()

label1 = tk.Button(root, bg='teal', text="Label 1")
label2 = tk.Button(root, bg='#820000', text="Label 2")
label3 = tk.Button(root, bg='#251749', text="Label 3")
label4 = tk.Button(root, bg='#562B08', text="Label 4")
label5 = tk.Button(root, bg='#FEC260', text="Label 5")
label6 = tk.Button(root, bg='#42032C', text="Label 6")


label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)
label4.grid(row=1, column=0)
label5.grid(row=1, column=1)
label6.grid(row=1, column=2)


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)


root.mainloop()

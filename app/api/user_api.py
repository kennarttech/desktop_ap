import tkinter as tk
import requests

class LoginGUI:
    def __init__(self, master):
        self.master = master
        master.title("Login")

        self.label_username = tk.Label(master, text="Username:")
        self.label_password = tk.Label(master, text="Password:")

        self.entry_username = tk.Entry(master)
        self.entry_password = tk.Entry(master, show="*")

        self.label_username.grid(row=0, sticky=tk.E)
        self.label_password.grid(row=1, sticky=tk.E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.logbtn = tk.Button(master, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.message = tk.Label(master, text="", fg="red")
        self.message.grid(columnspan=2)



    def _login_btn_clicked(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        response = requests.post("http://localhost:5000/login", json={"username": username, "password": password})

        if response.status_code == 200:
            self.message.config(text="Login successful", fg="green")
            self.master.destroy()
            if response.json()["is_admin"]:
                admin_dashboard = AdminDashboardGUI()
                admin_dashboard.run()
        else:
            self.message.config(text="Login failed", fg="red")



class AdminDashboardGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Admin Dashboard")

        self.label = tk.Label(self.window, text="Welcome Admin!")
        self.label.pack()

        self.button = tk.Button(self.window, text="View All Data", command=self._view_all_data)
        self.button.pack()

        self.label = tk.Label(self.window, text='', bg='teal')
        self.label.pack()


    def run(self):
        self.window.mainloop()

    def _view_all_data(self):
        response = requests.get("http://127.0.0.1:5000/students")
        
        if response.status_code == 200:
            data = response.json()
            for item in data:
                print(item)
                self.label['text'] = (item)


            

if __name__ == '__main__':
    root = tk.Tk()
    login = LoginGUI(root)
    root.mainloop()

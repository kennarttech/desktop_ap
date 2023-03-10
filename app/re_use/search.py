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

        self.signup_btn = tk.Button(master, text="Signup", command=self._signup_btn_clicked)
        self.signup_btn.grid(columnspan=2)

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
                admin_window = tk.Tk()
                admin_dashboard = AdminDashboardGUI(admin_window)
                admin_dashboard.run()
        else:
            self.message.config(text="Login failed", fg="red")

    def _signup_btn_clicked(self):
        signup_window = tk.Toplevel(self.master)
        SignupGUI(signup_window)



class SignupGUI:
    def __init__(self, master):
        self.master = master
        master.title("Signup")

        self.label_username = tk.Label(master, text="Username:")
        self.label_password = tk.Label(master, text="Password:")

        self.entry_username = tk.Entry(master)
        self.entry_password = tk.Entry(master, show="*")

        self.label_username.grid(row=0, sticky=tk.E)
        self.label_password.grid(row=1, sticky=tk.E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.signup_btn = tk.Button(master, text="Signup", command=self._signup_btn_clicked)
        self.signup_btn.grid(columnspan=2)

        self.message = tk.Label(master, text="", fg="red")
        self.message.grid(columnspan=2)

    def _signup_btn_clicked(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        response = requests.post("http://localhost:5000/signup", json={"username": username, "password": password})

        if response.status_code == 200:
            self.message.config(text="Signup successful", fg="green")
            self.master.destroy()
        else:
            self.message.config(text="Signup failed", fg="red")



class AdminDashboardGUI:
    def __init__(self, master):
        self.master = master
        master.title("Admin Dashboard")

        self.label = tk.Label(master, text="Welcome Admin!")
        self.label.pack()

        self.button = tk.Button(master, text="View All Data", command=self._view_all_data)
        self.button.pack()

        self.label = tk.Label(master, text='', bg='teal')
        self.label.pack()

        self.logout_btn = tk.Button(master, text="Logout", command=self._logout)
        self.logout_btn.pack()

    def _logout(self):
        self.master.destroy()

    def _view_all_data(self):
        response = requests.get("http://127.0.0.1:5000/data")

        if response.status_code == 200:
            data = response.json()
            text = ""
            for item in data:
                text += f"Name: {item['name']}, Age: {item['age']}, GPA: {item['gpa']}\n"
                self.label.config(text=text)

    def run(self):
        self.master.mainloop()



if __name__ == '__main__':
    root = tk.Tk()
    login = LoginGUI(root)
    root.mainloop()

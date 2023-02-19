import json
import hashlib
import tkinter as tk
from tkinter import messagebox



txt = 'app/users.json'
def authenticate(username, password):
    # Open the JSON file and load the contents into a dictionary
    with open(file=txt, mode='r') as f:
        users = json.load(f)
    
    # Check if the entered username exists in the dictionary
    if username in users:
        # Hash the entered password using SHA-256
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        # Check if the hashed password matches the value in the dictionary for the entered username
        if hashed_password == users[username]:
            return True
    
    return False

def login():
    # Retrieve the username and password entered by the user
    username = username_entry.get()
    password = password_entry.get()
    
    # Authenticate the user
    if authenticate(username, password):
        messagebox.showinfo("Login", "Login successful!")
    else:
        messagebox.showerror("Login", "Invalid username or password.")
        
# Create the main window
root = tk.Tk()
root.title("Login")

# Create the username label and entry field
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Create the password label and entry field
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create the login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

# Start the main loop
root.mainloop()

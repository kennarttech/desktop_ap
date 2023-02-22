import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Create the table view
table = ttk.Treeview(root, columns=('Name', 'Age', 'Country'))

# Set the column headings
table.heading('#0', text='ID')
table.heading('Name', text='Name')
table.heading('Age', text='Age')
table.heading('Country', text='Country')

# Add some rows
table.insert('', 'end', text='1', values=('Alice', 25, 'USA'))
table.insert('', 'end', text='2', values=('Bob', 30, 'Canada'))
table.insert('', 'end', text='3', values=('Charlie', 20, 'Australia'))

# Pack the table view
table.pack()

root.mainloop()

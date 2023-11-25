

import tkinter as tk
from tkinter import ttk

def button_click():
    print("Button clicked")

root = tk.Tk()

# create a treeview with columns
tree = ttk.Treeview(root, columns=("column1", "column2"))
tree.heading("#0", text="Item")
tree.heading("#1", text="Sr. No.")
tree.heading("#2", text="Button")

# add some sample data
for i in range(1, 6):
    btn = tk.Button(root, text="Attendance", command=button_click)
    btn.pack()
    tree.insert("" , "end" , values=btn)
# display the treeview
tree.pack()

root.mainloop()


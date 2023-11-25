# import tkinter as tk

# root = tk.Tk()

# # Create a StringVar object
# message_var = tk.StringVar()

# # Create a message widget and associate it with the StringVar object
# message_widget = tk.Message(root, textvariable=message_var)
# message_widget.pack()

# # Set the value of the StringVar object
# message_var.set("Hello, world!")

# # Retrieve the value of the StringVar object and store it in a variable
# message_value = message_var.get()

# # Print the value of the variable
# print(message_value)

# root.mainloop()


# import tkinter as tk
# from tkinter import ttk

# # create a Tkinter window
# root = tk.Tk()

# # create a Treeview widget
# tree = ttk.Treeview(root)

# # define columns for the Treeview widget
# tree["columns"] = ("Name", "Age", "Gender")

# # format column headers
# tree.heading("#0", text="ID")
# tree.column("#0")
# tree.heading("Name", text="Name")
# tree.column("Name")
# tree.heading("Age", text="Age")
# tree.column("Age")
# tree.heading("Gender", text="Gender")
# tree.column("Gender")

# # insert data into the Treeview widget
# tree.insert("", "end", text="1", values=("Alice", "25", "F"))
# tree.insert("", "end", text="2", values=("Bob", "30", "M"))
# tree.insert("", "end", text="3", values=("Charlie", "35", "M"))
# tree.insert("", "end", text="4", values=("David", "40", "M"))

# # pack the Treeview widget
# tree.pack()

# # start the Tkinter event loop
# root.mainloop()

# import tkinter as tk

# # Create a tkinter window
# root = tk.Tk()

# # Set window size
# root.geometry('500x500')

# # Create a label for "good morning"
# lbl_greeting = tk.Label(root, text="Good Morning", font=("Helvetica", 18), bg="blue", fg="white")

# # Add label to the window using grid
# lbl_greeting.grid(row=0, column=1, columnspan=3, sticky='ew')

# # Add other widgets to the window as needed using grid

# # Start the tkinter event loop
# root.mainloop()


import tkinter as tk

root = tk.Tk()

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)

file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

root.mainloop()

# from tkinter import *
# w = Tk()
# name = StringVar()
# number = StringVar()

# Label(w , text="Enter your name : " ).grid(row=0 , column=0)
# Label(w , text="Enter your enrolment number  : ").grid(row=1, column=0)

# name_box = Entry(w, textvariable=name, width=50 , borderwidth=5).grid(row=0 , column=1)
# num_box = Entry(w , textvariable=number, width=50 , borderwidth=5).grid(row=1 ,column=1 )

# def submit():
#     Label(f"my name is {name.get()}").grid(row= 2, column=0)
#     Label(f"my enrolment is {number.get()}").grid(row= 1, column = 1)

# Button(w , text="submit" , command = submit).grid(row=2 , column=1)
# w.mainloop()

# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox
# import mysql.connector

# def submit():
#     print(checkbox.get())
    
#     # pass

# window = tk.Tk()
# window.title("My Window")

# # selected_option = tk.StringVar()
# # global checkbox_values

# checkbox_values = []

# var = tk.BooleanVar()
# for i in range(10):
#     checkbox = tk.Checkbutton(window, text=f"Checkbox {i+1}", variable=var)
#     checkbox.pack()
    
# # for machine in enable:
# #     l = tk.Checkbutton(window, text=machine, onvalue=1,offvalue=0)
# #     cklist.append(l)
# #     l.pack()
    
# # Create a submit button that calls the submit function
# submit_button = tk.Button(window, text="Submit", command=submit)
# submit_button.pack()

# # Run the main event loop
# window.mainloop()


import tkinter as tk

root = tk.Tk()

# create a list to store checkbox values
checkbox_values = []

# create 10 checkboxes using a for loop
for i in range(10):
    var = tk.BooleanVar()
    checkbox = tk.Checkbutton(root, text=f"present", variable=var)
    checkbox.pack()
    checkbox_values.append(var)

# function to print checkbox values
def print_checkbox_values():
    for i, var in enumerate(checkbox_values):
        print(f"Checkbox {i+1}: {var.get()}")

# create a button to print checkbox values
button = tk.Button(root, text="Print Checkbox Values", command=print_checkbox_values)
button.pack()

root.mainloop()


# import tkinter as tk

# root = tk.Tk()

# # create some check boxes
# checkbox1 = tk.Checkbutton(root, text="Checkbox 1")
# checkbox2 = tk.Checkbutton(root, text="Checkbox 2")
# checkbox3 = tk.Checkbutton(root, text="Checkbox 3")

# # pack the check boxes into the GUI
# checkbox1.pack()
# checkbox2.pack()
# checkbox3.pack()

# # define a function to remove all the check boxes
# def remove_checkboxes():
#     for widget in root.winfo_children():
#         if isinstance(widget, tk.Checkbutton):
#             widget.destroy()

# # create a button to trigger the removal of the check boxes
# remove_button = tk.Button(root, text="Remove Checkboxes", command=remove_checkboxes)
# remove_button.pack()

# root.mainloop()


import mysql.connector 
mydb = mysql.connector.connect(host='localhost', user='root' , password='' , database='attandance')
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM ce_c")
data = mycursor.fetchall()

print(data[0])

#for row in data:
 #   print(row)
 
    
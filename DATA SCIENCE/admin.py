# import matplotlib.pyplot as plt
# import pandas as pd
import tkinter as tk
import mysql.connector
import tkinter.font as tkfont
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry


def login():
    t_id = id_entry.get()
    t_pswd = password_entry.get()

    # Do login validation here
    # if t_id == 'snehal_sir' and t_pswd == 'python':
    if True :
        if messagebox.showinfo("Message", "Login Successful"):
            # make other window
            root2 = tk.Tk()
            root2.geometry('600x500')
            menu_bar = tk.Menu(root2)
            title_label = tk.Label(root2, text="Snehal sir Schedule", font=("Arial", 20), bg="red", fg="white")
            title_label.grid(row= 0, column=0 )

            def attendance ():
                root3 = tk.Tk()
                def fill_att():
                    selected_day = day_combobox2.get()
                    if selected_day == 'Select Day':
                        messagebox.showinfo("Message", "Pls Select Proper Day")
                    else :
                        mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="",
                            database='attendance'
                        )
                        # mycursor = mydb.cursor()
                        # mycursor
                        
                days2 = ['Select Day For Attendance','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
                day_combobox2 = ttk.Combobox(root3, values=days2)
                day_combobox2.current(0)
                day_combobox2.grid(row = 1, column=0)
                # day_combobox.place(x=40,y=40)
                button = tk.Button(root3, text="Show Schedule", command=fill_att)
                button.grid(row = 2, column=0)
                root3.mainloop()
                
            def analysis():
                pass
            
            def check_scheduling():
                selected_day = day_combobox.get()
                if selected_day == 'Select Day':
                    messagebox.showinfo("Message", "Pls Select Proper Day")
                else :
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database='teachers'
                    )
                    mycursor = mydb.cursor()
                    mycursor.execute("select `starting_time` ,`ending_time`, `session_type`, `class_lab`, `division`  from  `teacher_course` where `day` = '{}'".format(selected_day))
                    data = mycursor.fetchall()
                    # print(data)
                    if data == [] :
                        messagebox.showinfo("Message", "No Session at that day")
                    else :
                        tree = ttk.Treeview(root2)
                        tree["columns"] = ("Starting time", "Ending time" ,"Session type" , "Class_Lab" , "Division" )

                        tree.heading("#0", text="Lecture No.")
                        tree.column("#0", width=100 , anchor="center")

                        tree.heading("Starting time", text="Starting time")
                        tree.column("Starting time", width=100 , anchor='center')

                        tree.heading("Ending time", text="Ending time")
                        tree.column("Ending time", width=100 , anchor='center')

                        tree.heading("Session type", text="Session type")
                        tree.column("Session type", width=100 , anchor='center')

                        tree.heading("Class_Lab", text="Class_Lab")
                        tree.column("Class_Lab", width=100 , anchor='center')

                        tree.heading("Division", text="Division") 
                        tree.column("Division", width=100 , anchor='center')
                        
                        j = 1 
                        for i in data :
                            tree.insert("", "end", text=j,values=i)
                            j+=1
                            tree.grid(row=3 , column =  0)
                
            # Create combobox with days of the week
            days = ['Select Day','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            day_combobox = ttk.Combobox(root2, values=days)
            day_combobox.current(0)
            day_combobox.grid(row = 1, column=0)
            # day_combobox.place(x=40,y=40)
            button = tk.Button(root2, text="Show Schedule", command=check_scheduling)
            button.grid(row = 2, column=0)
 
            menu = tk.Menu(menu_bar, tearoff=0)
            menu.add_command(label="Attendance" ,command=attendance)
            menu.add_command(label="Analysis" , command=analysis)
            menu.add_command(label="Exit" , command=root2.quit)
            menu_bar.add_cascade(label="Menu", menu=menu)
            root2.config(menu=menu_bar)
            root2.mainloop()

    elif t_id == 'bhumi_medam' and t_pswd == 'py2' :
        if messagebox.showinfo("Message", "Login Successful"):
            pass

    else:
        m = messagebox.showinfo("Message", "Pls Enter Field Details")
        print(m)
        
# Create a tkinter window
root = tk.Tk()
root.geometry('225x100')

# Create the login form widgets
id_label = tk.Label(root, text='Teacher Name : ')
id_label.grid(row = 0 , column= 0 , pady=5)

id_entry = tk.Entry(root)
id_entry.grid(row = 0 , column= 1)

password_label = tk.Label(root, text='Password : ')
password_label.grid(row = 1 , column= 0, pady=5)

password_entry = tk.Entry(root, show='*'  )
password_entry.grid(row = 1 , column= 1)

login_button = tk.Button(root, text='Login', command=login)
login_button.grid(row = 3 , column= 0 , pady=5)


# Start the tkinter event loop
root.mainloop()

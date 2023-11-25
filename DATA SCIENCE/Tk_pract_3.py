import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry

tlist = []
global text_box

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database='attendance'
)
mycursor = mydb.cursor()
w = tk.Tk()

def DataBasedOnDate():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database='attendance'
    )
    mycursor = mydb.cursor()

    def text():
        text_box.destroy()
        clear_c.destroy()
        scrollbar.destroy()
    
    s = date_entry.get()
    mycursor.execute("SELECT * FROM `final_att` where `date` = '{}' ".format(s))
    
    # mycursor.execute("SELECT * FROM `final_att` where `date` = '18/03/2023' ")
    data = mycursor.fetchall()
    # print(data)

    text_box = tk.Text(w, height=5, width=15)

    scrollbar = tk.Scrollbar(w)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    text_box.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=text_box.yview)

    text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    for row in data:
        text_box.insert(tk.END, row)
        text_box.insert(tk.END, "\n")
   
    
    clear_c = tk.Button(w, text="Clear record", command=text)
    clear_c.pack()
    
    
date_entry = DateEntry(w, width=12, background='darkblue', foreground='white', date_pattern='dd/MM/yyyy')
date_entry.pack()
    
select_table = tk.Button(w, text="Show Record", command=DataBasedOnDate)
select_table.pack()

w.mainloop()
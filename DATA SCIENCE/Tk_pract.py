import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
import mysql.connector
import tkinter.font as tkfont
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

tlist = []
global text_box 
checkbox_values = []

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database='attendance'
)

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES FROM attendance")

tables = mycursor.fetchall()
for table in tables:
    tlist.append(table)
    # print(tlist)
    
w = tk.Tk()
w.geometry("1400x600")
tbs = tk.StringVar()
en = tk.StringVar()
box_font = tkfont.Font(size = 12) 

def view_data():
                        
    def remove_attr(): 
        clear_con.destroy()
        submit_record.destroy()
        date_entry.destroy()
        label.destroy()
        session.destroy()
        label2.destroy()
        for widget in w.winfo_children():
            if isinstance(widget, tk.Checkbutton):
                widget.destroy()
        # tlist = []
        # checkbox_values = []
        
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database='attendance'
    )
    mycursor = mydb.cursor()
    # data = 0
    tbl_name = tbs.get()
    
    # if table empty then show message
    # if not tbl_name :
        # messagebox.showinfo("Message", "Pls Select Table First !")
    # else :
    data = 0
    mycursor.execute("SELECT `student_name`,`student_rollno`,`student_entrollment` FROM {} where 1".format(tbl_name))
    data = mycursor.fetchall()
    i = 0
    checkbox_values = []
    for row in data: 
        var = tk.BooleanVar()
        checkbox = tk.Checkbutton(w, text=row , variable=var , onvalue=True , offvalue=False , font=box_font)
        checkbox_values.append(var)
        # checkbox.pack()
        checkbox.grid(row=i, column=2, padx=100)
        i+=1
            
    def store():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database='attendance'
        )
        mycursor = mydb.cursor()    
        values = []
        check = False
        if True in checkbox_values :
            check = True
        
        for i in range (len(checkbox_values)):
            if checkbox_values[i].get() == True :
                # print("data = {0}".format(data[i]))
                
                values.append(str(date_entry.get()))
                values.append(str(session.get()))
                values.append("1")
                values.append(tbl_name)
                # print(tuple(list(data[i])+values))
                dt = tuple(list(data[i])+values)
                query = "INSERT INTO `final_att` (`student_name`,`student_rollno`,`student_enroll`,`date`,`session`,`present`,`div`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                x = mycursor.execute(query  ,dt)
                values = []
                if x :
                    pass
                else :
                    check+=1
        if check :
            messagebox.showinfo("Message", "Record Inserted")
            mycursor.close()
            mydb.commit()
        else:
            messagebox.showinfo("Message", "There is 0 Record Inserted")
            
    label = tk.Label(w, text="Enter date:")   
    label.grid(row=0, column=3, padx=5, pady=5)
    # label.pack(padx=5)

    date_entry = DateEntry(w, width=12, background='darkblue', foreground='white', date_pattern='dd/MM/yyyy')
    date_entry.grid(row=0, column=4, padx=5, pady=5)
    
    # date_entry.pack(padx=5, pady=5)
    
    label2 = tk.Label(w, text="Enter Session No. : ")
    label2.grid(row=1, column=3, padx=5, pady=5)
    
    # label2.pack()

    session = tk.Entry(w)
    session.grid(row=1, column=4, padx=5, pady=5)
    
    # session.pack()
    
    clear_con = tk.Button(w, text="Clear" , command=remove_attr , bg="red")
    clear_con.configure(fg="white")
    clear_con.grid(row=2, column=3, padx=5, pady=5)
    
    # clear_con.pack()
    
    submit_record = tk.Button(w, text="Entry ", command=store , bg="green")
    submit_record.configure(fg="white") 
    submit_record.grid(row=2, column=4, padx=5, pady=5)
    # submit_record.pack()


 
database_combobox = ttk.Combobox(w, textvariable=tbs, values=tlist )
database_combobox.grid(row=0, column=0, padx=5, pady=5)
# database_combobox.place(x=0, y=0, width=100, height=25)
# database_combobox.pack()

select_table = tk.Button(w, text="Show Record", command=view_data ,  bg="green")
select_table.configure(fg="white")
select_table.grid(row=1, column=0, padx=5, pady=5)


def analysis():
    # dt1 = dt1_lb.get()
    # dt2 = dt2_lb.get()
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database='attendance'
    )
    enrl = en.get()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT `date`,`student_rollno`,`student_name`,`student_enroll`,`session`,`present`,`div` FROM `final_att` where 1 ")
    df = mycursor.fetchall()
    df = pd.DataFrame(df , columns=["date" , "student_rollno" , "student_name" ,"student_enroll" , "session" , "present","div" ])
    x = df.groupby(["student_enroll",'date', "student_name"])['present'].sum().reset_index()
    x = x[x.student_enroll == enrl]
    
    # fig = plt.Figure(figsize=(2,2))
    print(x)
    plt.bar(x.date , x.present ,color="c" )
    plt.xlabel(f"{enrl} : {x.student_name.unique()[0]}")
    plt.ylabel("Total Present")
    plt.show()


label4 = tk.Label(w, text="Analyze Data " , fg="red" ,bg= "yellow" ).grid(row=3, column=0, padx=5, pady=10)

en_lb = tk.Label(w, text="Enter Enrollment No : " , fg="red" , ).grid(row=4, column=0, padx=5, pady=5)
enrollment_sch = ttk.Entry(w , textvariable=en).grid(row=4, column=1, padx=2, pady=5)    

# dt1_lb = tk.Label(w, text="Enter Starting Date : " , fg="red" ).grid(row=5, column=0, padx=2, pady=4)
# date1 = DateEntry(w, width=12, background='darkblue', foreground='white', date_pattern='dd/MM/yyyy').grid(row=5, column=1, padx=2, pady=4)

# dt2_lb = tk.Label(w, text="Enter Starting Date : " , fg="red" ).grid(row=6, column=0, padx=2, pady=4)
# date2 = DateEntry(w, width=12, background='darkblue', foreground='white', date_pattern='dd/MM/yyyy').grid(row=6, column=1, padx=2, pady=4)

analyze = tk.Button(w, text="Go To Analysis", command=analysis ,  bg="green").grid(row=7, column=0, padx=5, pady=5)

# label3 =  tk.Label(w, text="Enter Session No. : ")
# label3.grid(row=1, column=3, padx=5, pady=5)

# select_table.place(y=30, width=100, height=25)
# select_table.pack(padx=5 , pady=5)

w.mainloop()






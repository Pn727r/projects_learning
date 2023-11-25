import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database='attendance'
)
mycursor = mydb.cursor()
mycursor.execute("SELECT `date`,`student_rollno`,`student_name`,`student_enroll`,`session`,`present`,`div` FROM `final_att` where 1 ")
df = mycursor.fetchall()
# for data in df :
    # print(data)
    # print(df)    

df = pd.DataFrame(df , columns=["date" , "student_rollno" , "student_name" ,"student_enroll" , "session" , "present","div" ])


# search_date =  DateEntry(w, width=12, background='darkblue', foreground='white', date_pattern='dd/MM/yyyy')
# search_date.grid(row=0, column=4, padx=5, pady=5)


# analyze = tk.Button(w, text="Show Record", command=analysis ,  bg="green")
# analyze.configure(fg="white")
# analyze.grid(row=1, column=0, padx=5, pady=5)
 

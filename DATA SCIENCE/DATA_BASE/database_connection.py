import mysql.connector

connection = mysql.connector.connect(host="localhost" ,user= "root" ,password="" )
if connection :
    print("connection established")
    mycursor=connection.cursor()
    # create database 
    #mycursor.execute('Create database pythondb')

    # see how many tables are there
    mycursor.execute('show databases')
    mycursor.execute('Create table studentlist(name varchar(200), enrollment int(20))')
    
    for dbs in mycursor:
        print(dbs)
else :
    print("connection not established")
    
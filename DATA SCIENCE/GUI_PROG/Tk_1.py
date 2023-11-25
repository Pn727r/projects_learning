from tkinter import *

# creating window like app
# it run infinite time until we not close it manualy
win = Tk()

win.title("CAR INTRO")

# for icon of window 
# win.iconbitmap("C:\\Users\\abc\\Pictures\\Screenshots\\icon.png")

l1 = Label(win , text = 'hi i am rolls royce' ,fg="blue", bg="yellow"  ).pack()
l2 = Label(win , text = 'you are not \nafford  me twice' , fg ="red" , bg='yellow').pack()


win.mainloop()
# need for hold the window 
# without this window open and shutdown within microsecond
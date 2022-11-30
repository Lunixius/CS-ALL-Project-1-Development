from tkinter import *
from tkcalendar import Calendar
import sqlite3
from turtle import bgcolor, color

with sqlite3.connect("registeration.db") as db:
    cursor=db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS reminder(id integer PRIMARY KEY AUTOINCREMENT, newSelectedDate text NOT NULL , newEventName integer NOT NULL   )""")

tkobj = Tk()

tkobj.geometry("500x600")
tkobj.title("Calendar reminder")

tkc = Calendar(tkobj,selectmode = "day",year=2022,month=1,date=1)

tkc.pack(pady=40)

def fetch_date():
    date.config(text = "Selected Date is: " + tkc.get_date())

but = Button(tkobj,text="Select Date",command=fetch_date, bg="black", fg='white')

but.pack()

date = Label(tkobj,text="",bg='black',fg='white')
date.pack(pady=20)

def add_new_reminder():
    
    newReminder = reminder.get()
    newDate = date.get() 

    cursor.execute("SELECT COUNT(*) from users WHERE reminder='" + newReminder + "'")
    result = cursor.fetchone()

    if int(result[0])> 0:
        error["text"] = " Error: Enter the valid info"
    else:
            error["text"]="Added new reminder"
            cursor.execute("INSERT INTO users(SelectedDate,EventName)VALUES(?,?)",(newReminder,newDate))
            db.commit()

error = Message(text="",width =160)
error.place(x=30,y=10)
error.config(padx=0)
    
label1=Label(text="Enter event/task")
label1.place(x=60 , y=350)
label1.config(bg='darkgrey', padx =0)

reminder=Entry(text="")
reminder.place(x=220,y=350,width=200,height=25)

label2=Label(text="Enter date (Month/Day/Year)")
label2.place(x=60 , y=390)
label2.config(bg='darkgrey', padx =0)

reminder=Entry(text="  /  /    ")
reminder.place(x=220,y=390,width=200,height=25)

button=Button(text="ADD REMINDER" , command=add_new_reminder)
button.place(x=200,y=480,width=100,height=25)
button.config(bg="darkgrey")

tkobj.mainloop()



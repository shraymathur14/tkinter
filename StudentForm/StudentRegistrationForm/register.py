from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
import time
import mysql.connector

my_con = mysql.connector.connect(
     host="localhost",
     user="root",
     password="root",
     database="login")

my_cur = my_con.cursor()

def clear_field():
    reg_entry.delete(0,len(reg_entry.get()))
    name_entry.delete(0,len(name_entry.get()))
    skill_entry.delete(0,len(skill_entry.get()))
    reg_entry.delete(0,len(reg_entry.get()))
    rel_entry.delete(0,len(rel_entry.get()))
    reg_entry.focus()

def entry_fields():
    REGNO = reg_entry.get()
    NAME = name_entry.get()
    BIRTH = str(dob.get_date())
    DATE = str(date_entry.get_date())
    SKILL = skill_entry.get()
    CLASS = clicked.get()
    REL = rel_entry.get()
    GENDER = temp.get()

    try:
        sql = "INSERT INTO STUDENTS(RegNo, Date, Name, DOB, Gender, Religion, Class, Skills) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        value = (REGNO, DATE, NAME, BIRTH, GENDER, REL, CLASS, SKILL)
        my_cur.execute(sql, value)
        my_con.commit()
        messagebox.showinfo("Success","Successfully Registered")
        clear_field()
        
    except:
        messagebox.showerror("Error","Failed")


def create():
    global time_label, window, name_entry, name_label, date_entry, date_label, reg_entry, reg_label, dob_label, dob
    global male, female, rel_entry, rel_label, clicked,class_entry, skill, skill_entry, temp

    window = Tk()
    window.geometry("1000x500+200+50")
    window.title("Student Registration")
    window.config(bg="#06283D")
    time_label = Label(text="", bg="#06283D", fg="white", font=("Courier",12))
    time_label.place(x=790, y=0)
    head_label = Label(text="STUDENT REGISTRATION", bg="pink", font=("Courier",20))
    head_label.place(x=345, y=30)
    time1()

    search = Entry(borderwidth=5, width=30)
    search.place(x=720, y=40)
    search_bt = Button(text="SEARCH")
    search_bt.place(x=930, y=40)

    reg_label = Label(text="Registration No.",font=("Courier",12), bg="#06283D", fg="white")
    reg_label.place(x=25, y=100)
    reg_entry = Entry(width=30)
    reg_entry.place(x=200, y=105)

    date_label = Label(text="Date",font=("Courier",12), bg="#06283D", fg="white")
    date_label.place(x=500, y=100)
    date_entry = DateEntry(width=15, font=("Arial",13))
    date_entry.place(x=590, y=100)

    name_label = Label(text="Full Name",font=("Courier",12), bg="#06283D", fg="white")
    name_label.place(x=25, y=150)
    name_entry = Entry(width=30)
    name_entry.place(x=200, y=150)

    dob_label = Label(text="DOB",font=("Courier",12), bg="#06283D", fg="white")
    dob_label.place(x=25, y=200)
    dob = DateEntry(width=15, font=("Arial",13))
    dob.place(x=200, y=200)

    temp = StringVar()
    gender = Label(text="Gender",font=("Courier",12), bg="#06283D", fg="white")
    gender.place(x=25, y=250)
    male = Radiobutton(text="Male", variable=temp, value="Male")
    male.place(x=200,y=250)
    male.selection_clear()
    female = Radiobutton(text="Female", variable=temp, value="Female")
    female.place(x=280,y=250)
    female.selection_clear()

    rel_label = Label(text="Religion",font=("Courier",12), bg="#06283D", fg="white")
    rel_label.place(x=500, y=150)
    rel_entry = Entry(width=30)
    rel_entry.place(x=590, y=150)


    options = ["1st Year",
            "2nd Year",
            "3rd Year",
            "4th Year"]

    clicked = StringVar()
    clicked.set("Select Class")
    class_label = Label(text="Class",font=("Courier",12), bg="#06283D", fg="white")
    class_label.place(x=500, y=200)
    class_entry = OptionMenu(window,clicked,*options)
    class_entry.place(x=590, y=200)

    skill = Label(text="Skills",font=("Courier",12), bg="#06283D", fg="white")
    skill.place(x=500, y=250)
    skill_entry = Entry(width=30)
    skill_entry.place(x=590,y=250)


    canva = Canvas(width=100, height=100, bg="White")
    canva.place(x=850, y=100)

    img_but = Button(text="Upload", width=15)
    img_but.place(x=850, y=220)

    save_but = Button(text="Save", width=20, font=("Arial",12), command=entry_fields)
    save_but.place(x=320, y=350)

    reset_but = Button(text="Reset", width=20, font=("Arial",12), command=clear_field)
    reset_but.place(x=570, y=350)

    window.mainloop()

#live time 
def time1():
        live_time = time.localtime()
        time_string = time.strftime("%d/%m/%Y, %H:%M:%S", live_time)    
        time_label.config(text=time_string)
        time_label.after(1000, time1)

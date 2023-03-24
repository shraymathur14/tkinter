import tkinter
from tkinter import messagebox
from register import create
import mysql.connector

my_con = mysql.connector.connect(
    host = "localhost", user = "root", password = "root", database = "login"
)
my_cur = my_con.cursor()


def entry_filled(val):
    if len(val) == 0:
        return False
    return True


def check_entry():
    name = name_entry.get()
    passwd = pass_entry.get()

    if entry_filled(name) and entry_filled(passwd):
        try:
            sql = f"Select * from credentials where UserName='{name}'"
            my_cur.execute(sql)
            res = my_cur.fetchall()
            if (res[0][0] == name and res[0][1] == passwd):
                login_win.destroy()
                create()
        except:
            messagebox.showerror("Error","Wrong Credentials")
            name_entry.delete(0,len(name))
            pass_entry.delete(0,len(name))
    else:
        if not entry_filled(name):
            messagebox.showerror("Error","Username cannot be empty")
            return
        elif not entry_filled(passwd):
            messagebox.showerror("Error","Password cannot be empty")
            return 



# def submit_data():
    # name = name_entry.get()
    # passwd = pass_entry.get()

    # if not entry_filled(name):
    #     messagebox.showerror("Error","Username cannot be empty")
    #     return
    # if not entry_filled(passwd):
    #     messagebox.showerror("Error","Password cannott be empty")
    #     return 

#     sql = "INSERT INTO CREDENTIALS(UserName, Password) VALUES(%s,%s)"
#     value = (name, passwd)
#     try:
#         my_cur.execute(sql, value)
#         my_con.commit()
#         name_entry.delete(0,len(name))
#         pass_entry.delete(0,len(passwd))
#         name_entry.focus()
#         messagebox.showinfo("showinfo","Successfully Registered")
#     except:
#         messagebox.showerror("showerror","Error!!!")
#     my_con.close()

def loginnn():
    global name_entry, pass_entry, login_win
    login_win = tkinter.Tk()
    login_win.title("LOGIN FORM")
    login_win.minsize(width=350, height=200)
    login_win.config(padx=100,pady=50)

    label_1 = tkinter.Label(text="Login Form", font=("Arial",30))
    label_1.grid(column=1, row=0)
    label_1.config(pady=10)

    name_label = tkinter.Label(text="Username", font=("Arial",10))
    name_label.grid(column=0, row=1)

    name_entry =tkinter.Entry()
    name_entry.grid(column=1,row=1)

    pass_label = tkinter.Label(text="Password", font=("Arial",10))
    pass_label.grid(column=0, row=2)

    pass_entry =tkinter.Entry(show="*")
    pass_entry.grid(column=1,row=2)

    submit_button = tkinter.Button(text="Submit", command=check_entry)
    submit_button.grid(column=1, row=3)

    login_win.mainloop()

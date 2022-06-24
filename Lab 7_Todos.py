import tkinter
import threading
from tkinter import messagebox
import sys

tasks = []
timer = threading
real_timer = threading
ok_thread = True
def getting_tasks(event=""):
    work = todo.get()
    hour = int(time.get())
    todo.delete(0, tkinter.END)
    time.delete(0, tkinter.END)
    todo.focus_set()
    adding_record(work, hour)
    if 0 < hour < 999:
       updating_record()


def adding_record(work, hrs):
    tasks.append([work, hrs])
    clock = threading.Timer(hrs, proceed_time, [work])
    clock.start()


def updating_record():
    if WorkingList.size() > 0:
       WorkingList.delete(0, "end")
    for task in tasks:
       WorkingList.insert("end", "" + task[0] + "=======>>> Time left: " + str(task[1]) + " Seconds")


def proceed_time(task):
    tkinter.messagebox.showinfo("Notification", "Its Now the Time for : " + task)


def actual_time():
    if ok_thread:
       real_timer = threading.Timer(1.0, actual_time)
       real_timer.start()
    for task in tasks:
     if task[1] == 0:
        tasks.remove(task)
        task[1] -= 1
        updating_record()


if __name__ == '__main__':
# application
   root = tkinter.Tk()
   root.geometry("460x480")
   root.title("Students to do List Reminder")
   root.rowconfigure(0, weight=1)
   root.config(bg="blue")


frame = tkinter.Frame(root)
frame.pack()

lbl = tkinter.Label(root, text="Enter Tasks To Do:", fg="white", bg="blue",
font=('Arial', 14), wraplength=200)
lbl_hrs = tkinter.Label(root, text="Enter time (Seconds)", fg="white",
bg="blue", font=('Arial', 14), wraplength=200)
todo = tkinter.Entry(root, width=30, font=('Arial', 14))
time = tkinter.Entry(root, width=15, font=('Arial', 14))
post = tkinter.Button(root, text='Add task', fg="white", bg='green',
font=('Arial', 16), relief="ridge", bd=5, height=3,
width=30, command=getting_tasks)
Exit = tkinter.Button(root, text='Exit', fg="white", bg='red', height=3,
font=('Arial Bold', 14), relief="ridge", bd=5, width=30, command=root.destroy)
WorkingList = tkinter.Listbox(root, font=('Arial', 12))
if tasks != "":
   actual_time()

root.bind('<Return>', getting_tasks)

lbl.place(x=0, y=10, width=200, height=25)
lbl_hrs.place(x=235, y=10, width=200, height=25)
todo.place(x=20, y=40, width=160, height=25)
time.place(x=245, y=40, width=170, height=25)
post.place(x=62, y=80, width=100, height=25)
Exit.place(x=302, y=80, width=50, height=25)
WorkingList.place(x=20, y=120, width=395, height=300)


root.mainloop()
ok_thread = False
sys.exit("FINISHED")

import tkinter as tk
from functools import partial

# global variable
tempVal = "Celsius"
# getting drop down value
def store_temp(sel_temp):
    global tempVal
    tempVal = sel_temp


# the main conversion
def call_convert(rlabel1, rlabe12, inputn):
    tem = inputn.get()
    if tempVal == 'Celsius':
        f = float((float(tem) * 9 / 5) + 32)
        k = float((float(tem) + 273.15))
        rlabel1.config(text="%f Fahrenheit" % f)
        rlabe12.config(text="%f Kelvin" % k)
    if tempVal == 'Fahrenheit':
        c = float((float(tem) - 32) * 5 / 9)
        k = c + 273
        rlabel1.config(text="%f Celsius" % c)
        rlabe12.config(text="%f Kelvin" % k)
    if tempVal == 'Kelvin':
        c = float((float(tem) - 273.15))
        f = float((float(tem) - 273.15) * 1.8000 + 32.00)
        rlabel1.config(text="%f Celsius" % c)
        rlabe12.config(text="%f Fahrenheit" % f)
    return
# app window configuration and UI
root = tk.Tk()
root.geometry('400x150+100+200')
root.title('Temperature Converter')
root.configure(background='#09A3BA')
root.resizable(width=False, height=False)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

numberInput = tk.StringVar()
var = tk.StringVar()

# label and entry field
input_label = tk.Label(root, text="Enter temperature", background='#09A3BA', foreground="#FFFFFF")
input_entry = tk.Entry(root, textvariable=numberInput)
input_label.grid(row=1)
input_entry.grid(row=1, column=1)

# result label's for showing the other two temperatures
result_label1 = tk.Label(root, background='#09A3BA', foreground="#FFFFFF")
result_label1.grid(row=3, columnspan=4)
result_label2 = tk.Label(root, background='#09A3BA', foreground="#FFFFFF")
result_label2.grid(row=4, columnspan=4)

# drop down initalization and setup
dropDownList = ["Celsius", "Fahrenheit", "Kelvin"]
dropdown = tk.OptionMenu(root, var, *dropDownList, command=store_temp)
var.set(dropDownList[0])
dropdown.grid(row=1, column=3)
dropdown.config(background='#09A3BA', foreground="#FFFFFF")
dropdown["menu"].config(background='#09A3BA', foreground="#FFFFFF")

# button click
call_convert = partial(call_convert, result_label1, result_label2, numberInput)
result_button = tk.Button(root, text="Convert", command=call_convert, background='#09A3BA', foreground="#FFFFFF")
result_button.grid(row=2, columnspan=4)

root.mainloop()




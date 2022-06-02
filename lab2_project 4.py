from tkinter import*
from tkinter import messagebox

attempts = 3
def login():
    username = user.get()
    pin = Pin.get()
    global attempts

    if (username== "" and pin==""):
        messagebox.showinfo("Error", "Please enter the username and pin")
    elif(username== "micha" and pin=="1927"):
        messagebox.showinfo("ATM","login successfully")
    else:
        messagebox.showerror("Error", "Incorrect Username/Pin" + "\n   Attempts left: " + str(attempts - 1))
        attempts -= 1
    if attempts == 0:
        messagebox.showerror("Error", "Incorrect Username/Pin" + "\nTransaction Failed!")


atm = Tk()
atm.title("ATM Login")
atm.geometry("500x300")
atm.resizable(0, 0)
global user
global Pin

Label(atm, text="Username:").place(x=110, y=63)
Label(atm, text="Pin:").place(x=110, y=105)

user=Entry(atm, bd=6)
user.place(x=200, y=60 )
Pin =Entry(atm, bd=6)
Pin.place(x=200, y=100)
Button(atm, text="Login", command=login, height=1, width=10, bd=6). place(x=200, y=150)
atm.mainloop()


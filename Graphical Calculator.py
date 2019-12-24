from tkinter import *
from tkinter import messagebox

import self

top = Tk()

global c

def donothing():
    x = 0


def help():
    messagebox.showinfo("Sorry",
                        "Sorry But this fature is not available in this version of software which you are using "
                        "please upadte your software")


def update():
    messagebox.showerror("Not Able to connect",
                         "Sorry!  But We are not able to connect the servers right now please download the latest "
                         "version manually from the website \n Website:- kiracloud.epizy.com")


def new():
    window = Toplevel(top)
    window.title("Message")
    messagebox.showwarning("Still Updating ", "Sorry But the work is currently going under work")


def ver():
    messagebox.showinfo("Version", "Developer : Alex Mercer \nVersion : 0.0.0.1 \nFlags : Non-Updatable")


top.title("Alex Mercer")

w = 350
h = 300

menubar = Menu(top)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: self.editor.event_generate('<Control-x>'))
editmenu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: self.editor.event_generate('<Control-c>'))
editmenu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: self.editor.event_generate('<Control-v>'))
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help", command=help)
helpmenu.add_command(label="Version", command=ver)
helpmenu.add_command(label="Update", command=update)
menubar.add_cascade(label="Help", menu=helpmenu)

Label(top, text="Enter Your First Number ").grid(row=0, padx=10, pady=20)
Label(top, text="     Enter Your Second Number ").grid(row=1, padx=10, pady=20)

f1 = IntVar
f2 = IntVar

f1 = Entry(top)
f2 = Entry(top)

f1.grid(row=0, column=1)
f2.grid(row=1, column=1)

def add():
    if (f1.get() and f2.get() != ""):
        try:
            num1 = float(f1.get())
            num2 = float(f2.get())
            answer = num1 + num2

            answer_label.configure(text=answer)
        except:
            messagebox.showerror("Error", "Please check your info entered and please enter correctly")
    else:
        messagebox.showinfo("INFO", " Please fill all the information")


def subs():
    if (f1.get() and f2.get() != ""):
        try:
            num1 = float(f1.get())
            num2 = float(f2.get())
            answer = num1 - num2

            answer_label.configure(text=answer)
        except:
            messagebox.showerror("Error", "Please check your info entered and please enter correctly")
    else:
        messagebox.showinfo("INFO", " Please fill all the information")


def mul():
    if (f1.get() and f2.get() != ""):
        try:
            num1 = float(f1.get())
            num2 = float(f2.get())
            answer = num1 * num2

            answer_label.configure(text=answer)
        except:
            messagebox.showerror("Error", "Please check your info entered and please enter correctly")
    else:
        messagebox.showinfo("INFO", " Please fill all the information")


def div():
    if (f1.get() and f2.get() != ""):
        try:
            num1 = float(f1.get())
            num2 = float(f2.get())
            answer = num1 / num2

            answer_label.configure(text=answer)
        except:
            messagebox.showerror("Error", "Please check your info entered and please enter correctly")
    else:
        messagebox.showinfo("INFO", " Please fill all the information")


result_text = Label(top, text="Result = ")
result_text.grid(row=2, column=1)

answer_label = Label(top, text="---")
answer_label.grid(row=2, column=3)

calculate_button = Button(top, text="ADD", command=add)
calculate_button.grid(row=5, column=0, columnspan=3, padx=10, pady=20)

calculate_button = Button(top, text="Substract", command=subs)
calculate_button.grid(row=5, column=1, columnspan=3, padx=20, pady=40)

calculate_button = Button(top, text="Multiply", command=mul)
calculate_button.grid(row=6, column=0, columnspan=3, padx=5, pady=10)

calculate_button = Button(top, text="Divide", command=div)
calculate_button.grid(row=6, column=1, columnspan=3)

top.config(menu=menubar)

top.geometry("{}x{}".format(w, h))

mainloop()
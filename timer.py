from tkinter import *
from tkinter import ttk
import datetime


def push():
    clo.delete(0, 'end')
    now = datetime.datetime.now()
    print(now.hour,now.minute,now.second)
    clo.insert(END,now)
    global b
    b = b + 1
    print(b)

root = Tk()
root.title("clock")
b = 0
clo = ttk.Entry(root)
clo.grid()

clob = Button(root,text="nowtime",command=push)
clob.grid()

root.mainloop()


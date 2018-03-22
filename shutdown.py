import subprocess
from tkinter import *
from tkinter import ttk

def function1(v1):
    if v1 == 'シャットダウン':
        cmd = 'shutdown -s -t 3600'
        return subprocess.call(cmd, shell = True)
    elif v1 == '再起動':
        cmd = 'shutdown -r -t 3600'
        return subprocess.call(cmd, shell = True)
    elif v1 == '中止':
        cmd = 'shutdown -a'
        return subprocess.call(cmd, shell = True)
    else:
        print ('だめ')

def button_click():
    show_selection()
    
def show_selection():
    for i in lb.curselection():
       function1(lb.get(i))

if __name__ == '__main__':
    root = Tk()
    root.title('shutdown timer')
    
    # シャットダウンフレーム
    frame1 = LabelFrame(root, text="Shutdown Menu")
    frame1.grid()
    # リストボックス
    currencies = ('シャットダウン', '再起動', '中止')
    v1 = StringVar(value=currencies)
    lb = Listbox(frame1, listvariable=v1,height=3)
    lb.grid(row=0, column=0)

    # ボックス
    
    #Button
    
    button1 = ttk.Button(frame1, text='OK', command=button_click)
    
    button1.grid(row=0, column=1)
    
    root.mainloop()
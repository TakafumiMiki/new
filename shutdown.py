import subprocess
from tkinter import *
from tkinter import ttk

def function1(v1):
    if v1 == 'シャットダウン':
        cmd = 'shutdown -s -t '
        return cmd
        #return subprocess.call(cmd, shell = True)
    elif v1 == '再起動':
        cmd = 'shutdown -r -t '
        return cmd
        #return subprocess.call(cmd, shell = True)
    elif v1 == '中止':
        cmd = 'shutdown -a'
        return cmd
        #return subprocess.call(cmd, shell = True)
    else:
        print ('だめ')

def button_click():
    show_selection()

def show_selection():
    for i in lb.curselection():
       function1(lb.get(i))

       #追加
def show_timecommand():
    try:
        if(function1(lb.get(lb.curselection())) != 'shutdown -a'):
            print(function1(lb.get(lb.curselection())) + str(v1.get()))
            
        else:
            print(function1(lb.get(lb.curselection())))

    except Exception:
        print("どちらかが指定されてないです")
"""
        if(function1(lb.get(lb.curselection())) is None):
            if(v1.get() is None):
                print("両方指定されてないです")
            elif():
                print("function1()が選択されてないです")
        elif(): 
            print("時間が選択されてないです")
"""

def rb_clicked():
    show_timecommand()

if __name__ == '__main__':
    root = Tk()
    root.title('shutdown timer')
    
    # シャットダウンフレーム
    frame1 = ttk.LabelFrame(root, text="Shutdown Menu")
    frame1.grid()

    # シャットダウンリストボックス
    currencies = ('シャットダウン', '再起動', '中止')
    v1 = StringVar(value=currencies)
    lb = Listbox(frame1, listvariable=v1,height=3)
    lb.grid(row=0, column=0)

    # シャットダウンボタン
    button1 = ttk.Button(frame1, text='OK', command=button_click)
    button1.grid(row=0, column=1)

    #↓ここからタイマー
    #タイマーフレーム
    timerframe = ttk.LabelFrame(root, text="Timer")
    timerframe.grid()

    #ラジオボタンで時間 分 秒 の指定
    v1 = IntVar()

    #時間(下の時間に*3600)
    rb1 = ttk.Radiobutton(
        timerframe,
        text = '時間',
        value = 3600,
        variable = v1)
    rb1.grid(row = 1,column = 0)

    #分(下の時間に*60)
    rb1 = ttk.Radiobutton(
        timerframe, 
        text = '  分  ',
        value = 60,
        variable = v1)
    rb1.grid(row = 2,column = 0)

    #秒(下の時間に*1)
    rb1 = ttk.Radiobutton(
        timerframe, 
        text = '  秒  ',
        value = 1,
        variable = v1)
    rb1.grid(row = 3,column = 0)

    #Button
    button2 = ttk.Button(
        timerframe, 
        text='OK', 
        padding=5,
        command=rb_clicked)
    button2.grid(row = 2,column=1)

    #タイマー入力
    EditBox = Entry(timerframe)
    EditBox.grid()
    EditBox.delete(0,END)

    root.mainloop()
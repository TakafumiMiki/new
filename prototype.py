import subprocess
from tkinter import *
from tkinter import ttk

def function1(v1):
    if v1 == 'シャットダウン':
        cmd = 'shutdown -s -t '

    elif v1 == '再起動':
        cmd = 'shutdown -r -t '
        
    elif v1 == '中止':
        cmd = 'shutdown -a'
        
    else:
        return print ('だめ')
    
    return cmd    

def button_click():
    show_selection()
    
def show_selection():
    for i in lb.curselection():
       function1(lb.get(i))

    #タイマーで追加
def show_timecommand():
    cmd1 = v2.get())

def rb_clicked():
    show_timecommand()

    #タイマー数値とコマンドを合体
def union(cmd,cmd1):#function1()のreturn と show_timecommandのreturn を合わせたい
    '''
    str(cmd1)
    timecmd = cmd + cmd1
    '''


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
    v2 = IntVar()
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
        variable = v2)
    rb1.grid(row = 2,column = 0)

    #秒(下の時間に*1)
    rb1 = ttk.Radiobutton(
        timerframe, 
        text = '  秒  ',
        value = 1,
        variable = v2)
    rb1.grid(row = 3,column = 0)

    #Button
    button2 = ttk.Button(
        timerframe, 
        text='OK', 
        padding=5,
        command=rb_clicked)
    button2.grid(row = 2,column=1)
    '''
    #タイマー入力
    EditBox = Entry(timerframe,text = "時間を入力")
    
    #EditBox.insert(END,"時間を入力")
    EditBox.grid()
    EditBox.delete(0,END)
    '''
    #時間とコマンドを足すためのボタン
    button3 = ttk.Button(
        timerframe, 
        text='union', 
        padding=5,
        command=union())
    )
    button3.grid(row=4)

    root.mainloop()
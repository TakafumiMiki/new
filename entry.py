from tkinter import *
from tkinter import ttk

def numclick():
    if num.get().isdigit() == True:#ここで数字だった場合v1.get()と掛け算を行う
        print(num.get())#ここで値を取得
        '''
        sel = num.get()*v1.get()
        return sel 
        '''
        num.delete(0, 'end')
        print(num.get())
        num.insert(END,"入力されました")
        print(num.get())
    else:
        print("数字じゃない") 


root = Tk()
root.title("1行入力で数値以外はじきたい")

label1 = Label(root,text="数値を入力",font=("",8))
label1.grid(row=0)

num = ttk.Entry(root)
num.grid(row=1, column=0)

numb = Button(root, text = "OK", command=numclick)
numb.grid(row=1, column=1)

root.mainloop()
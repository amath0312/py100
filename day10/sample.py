# -*- coding:utf8 -*-

import tkinter
from tkinter import messagebox

def gui_main():
    """GUI demo"""
    flag = True
    def change_label_msg():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, world!')\
            if flag else ('blue', 'Goodbye, world!')
        label.config(text=msg, fg=color)


    def confirm_to_quit():
        if messagebox.askokcancel('温馨提示', '确认退出吗'):
            top.quit()

    top = tkinter.Tk()
    #宽x长+x+y
    top.geometry('200x300+100+100')
    top.title('小游戏')
    # top.attributes('-topmost',1)
    label = tkinter.Label(top, text='hello world', font='consolas 16')
    label.pack(expand=1)

    panel = tkinter.Frame(top)
    bt1 = tkinter.Button(top, text='修改', command=change_label_msg)
    bt1.pack(side='left')

    bt2 = tkinter.Button(top, text='退出', command=confirm_to_quit)
    bt2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == "__main__":
    gui_main()

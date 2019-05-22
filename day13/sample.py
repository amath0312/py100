# -*- coding:utf8 -*-

import tkinter
import tkinter.messagebox
import time
from threading import Thread
from multiprocessing import Process, Queue


def download():
    class DownloadHandler(Thread):

        def run(self):
            time.sleep(5)
            tkinter.messagebox.showinfo('提示', '下载完成')
            bt1.config(state=tkinter.NORMAL)

    def download():
        bt1.config(state=tkinter.DISABLED)
        DownloadHandler(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('关于', '作者: Emmm(v1.0)')

    tk = tkinter.Tk()
    tk.geometry('200x100')
    tk.title('单线程')
    tk.wm_attributes('-topmost', 1)

    panel = tkinter.Frame(tk)
    bt1 = tkinter.Button(panel, text='下载', command=download)
    bt1.pack(side='left')
    bt2 = tkinter.Button(panel, text='关于', command=show_about)
    bt2.pack(side='right')
    panel.pack(side='bottom')

    tk.mainloop()


def summary_task(numbers, queue):
    sum = 0
    for num in numbers:
        sum += num
    queue.put(sum)

def summary():
    process_cnt = 8
    max = 100000000
    number_range = max//process_cnt
    numbers = [x for x in range(1, max)]
    queue = Queue()
    processes = []
    
    start = time.time()
    for i in range(process_cnt):
        process = Process(target=summary_task, args=(numbers[i*number_range:(i+1)*number_range], queue))
        process.start()
        processes.append(process)
    for process in processes:
        process.join()

    sum = 0
    while not queue.empty():
        sum += queue.get()
        
    end = time.time()
    print('总耗时 %.2f, 结果 %d' % (end - start, sum))# 4999999950000000

def main():
    # download()
    summary()

if __name__ == "__main__":
    main()

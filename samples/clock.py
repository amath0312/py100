# -*- coding:utf8 -*-

import os
import sys
import threading
import time
import tkinter


class Clock(object):

    def __init__(self, render=None):
        self._render = render
        self._max = -1
        self._thread = None
        self._running = False
        self._render_template = '00:00:00 .000'

    @property
    def render(self):
        return self._render

    @render.setter
    def render(self, render):
        self._render = render

    def stop(self):
        if self._render:
            self._render(self._render_template)
        else:
            os.system('clear')
            print(self._render_template)

        self._render_template = '00:00:00 .000'
        self._running = False
        self._thread = None

    def start(self, max=-1):
        if self._running:
            return

        self._max = max
        self._thread = threading.Thread(
            target=Clock._timer_tick, args=(self, ), daemon=True)
        self._running = True
        self._thread.start()

    def rend_timer(self, start, end):
        ''' 计算计时时间并渲染计时器 '''
        if not self._running:
            return 
        hour, minute, second, ms = Clock._parse_time(start, end)
        self._rend(hour, minute, second, ms)        

    @staticmethod
    def _timer_tick(clock):
        ''' 定时刷新计时器 '''
        start = time.time()
        while clock._running and (clock._max == -1 or (time.time() - start) <= clock._max):
            time.sleep(0.1)
            render_tmpl = clock.rend_timer(start, time.time())
            
        clock._running = False
        clock._thread = None

    def _rend(self, hour, minute, second, ms):
        ''' 渲染计时器 '''
        self._render_template = '%02d:%02d:%02d .%03d' % (hour, minute, second, ms)
        if self._render:
            self._render(self._render_template)
        else:
            os.system('clear')
            print(self._render_template)

    @staticmethod
    def _parse_time(start, end):
        ''' 计算出计时器当前计时（时、分、秒、毫秒） '''
        dur = int((end - start) * 1000 // 1)

        ms = int(dur % 1000)

        dur = dur // 1000
        second = dur % 60

        dur = dur // 60
        minute = dur % 60

        dur = dur // 60
        hour = dur
        return hour, minute, second, ms

def listen():
    while(True):
        action = input()
        if action.lower() == 'q':
            break
    sys.exit(0)


def clock_term(max=-1):
    clock = Clock()
    clock.start(max=max)

    listen()


def clock_gui():
    clock = Clock()
    root = tkinter.Tk()
    root.title('计时器')
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    w = 300
    h = 300
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(width=False, height=False)

    tkinter.Label(root, height=2).pack(side='top')

    label = tkinter.Label(root, text='00:00:00 .000', height=3,
                          font='"Source Han Sans SC Light" -42 underline', anchor='center')
    label.pack()

    panel = tkinter.Frame(root)
    tkinter.Button(panel, text='启动', font='"Source Han Sans SC Light" -16',
                   command=clock.start).pack(side='left', padx=10)
    tkinter.Button(panel, text='停止', font='"Source Han Sans SC Light" -16',
                   command=clock.stop).pack(side='right', padx=10)
    panel.pack()
    tkinter.Label(root).pack(side='bottom')

    clock.render = lambda s: label.config(text=s)
    # clock.start()

    root.mainloop()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'term':
        max = -1
        if len(sys.argv) > 2:
            max = int(sys.argv[2].strip())
        clock_term(max)
    else:
        clock_gui()

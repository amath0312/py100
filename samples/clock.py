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

    @property
    def render(self):
        return self._render

    @render.setter
    def render(self, render):
        self._render = render

    def stop(self):
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

    @staticmethod
    def _timer_tick(clock):
        start = time.time()
        while clock._running and (clock._max == -1 or (time.time() - start) <= clock._max):
            time.sleep(0.1)
            render_tmpl = Clock._rend_timer(start, time.time())
            if clock._render:
                clock._render(render_tmpl)
            else:
                os.system('clear')
                print(render_tmpl)
        clock._running = False
        clock._thread = None

    @staticmethod
    def _rend_timer(start, end):
        dur = int((end - start) // 1)

        second = dur % 60

        dur = dur // 60
        minute = dur % 60

        dur = dur // 60
        hour = dur

        return '%02d:%02d:%02d' % (hour, minute, second)


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
    w = 200
    h = 200
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(width=False, height=False)

    tkinter.Label(root, height=2).pack(side='top')

    label = tkinter.Label(root, text='00:00:00', height=3,
                          font='"Source Han Sans SC Light" -24 underline', anchor='center')
    label.pack()

    panel = tkinter.Frame(root)
    tkinter.Button(panel, text='启动', font='"Source Han Sans SC Light" -16',
                   command=clock.start).pack(side='left')
    tkinter.Button(panel, text='停止', font='"Source Han Sans SC Light" -16',
                   command=clock.stop).pack(side='right')
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

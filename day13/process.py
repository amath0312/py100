# -*- coding: utf8 -*-

import time
import random
from multiprocessing import Process, Queue
from os import getpid



def download_sigle_process():
    start = time.time()
    download_file('文件1.txt')
    download_file('文件2.txt')
    end = time.time()
    print('总共耗时 %.2f 秒'% (end-start))


def download_muilt_process():
    start = time.time()
    p1 = Process(target=download_file, args=('文件1.txt',))
    p2 = Process(target=download_file, args=('文件2.txt',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    print('总共耗时 %.2f 秒'% (end-start))


def download_file(filename):
    print('开始下载 %s'%filename)
    time_to_download = random.randint(5, 10)
    time.sleep(time_to_download)
    print('%s 下载完成，共耗时 %d 秒' % (filename, time_to_download))


def ping_pong():
    queue = Queue()
    for i in range(10):
        queue.put(i)
    p1 = Process(target=ping_pong_sub_task, args=('ping', queue))
    p2 = Process(target=ping_pong_sub_task, args=('pong', queue))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print()

def ping_pong_sub_task(string, queue):
    while not queue.empty():
        queue.get(False)
        print(string, end=' ', flush=True)
        time.sleep(random.random())


def main():
    # download_sigle_process()
    # download_muilt_process()
    ping_pong()

if __name__ == '__main__':
    main()
    
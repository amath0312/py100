# -*- coding: utf8 -*-

import time
import random
from threading import Thread


class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载 %s' % self._filename)
        time_to_download = random.randint(2, 5)
        time.sleep(time_to_download)
        print('%s 下载完成，共耗时 %d 秒' % (self._filename, time_to_download))

def download_multi_thread2():
    start = time.time()
    t1 = DownloadTask('file1.pdf')
    t2 = DownloadTask('file2.pdf')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()
    print('总共耗时 %.2f 秒' % (end - start))


def download_muilt_thread():
    start = time.time()
    t1 = Thread(target=download_file, args=('file1.txt',))
    t2 = Thread(target=download_file, args=('file2.txt',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()
    print('总共耗时 %.2f 秒' % (end - start))


def download_file(filename):
    print('开始下载 %s' % filename)
    time_to_download = random.randint(5, 10)
    time.sleep(time_to_download)
    print('%s 下载完成，共耗时 %d 秒' % (filename, time_to_download))


def main():
    # download_muilt_thread()
    download_multi_thread2()


if __name__ == '__main__':
    main()

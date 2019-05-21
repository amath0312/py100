# -*- coding: utf-8 -*-

import time
import os
import sys


class Clock(object):
    """
    数字时钟
    """

    def __init__(self, hour=0, minute=0, second=0):
        """
        初始化数字时钟
        :param hour: 小时
        :param minute: 分钟
        :pararm second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    def tick(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1

            if self._minute == 60:
                self._minute = 0
                self._hour += 1

                if self._hour == 24:
                    self._hour = 0

    def display(self):
        os.system('clear')
        print('%02d:%02d:%02d' % (self._hour, self._minute, self._second))

import math
class Point(object):
    """平面上的点"""

    def __init__(self, x=0, y=0):
        """定义点的初始位置, 默认坐标为原点(0, 0)"""
        self._x = x
        self._y = y
    
    def move_to(self, x, y):
        """移动到指定坐标"""
        self._x = x
        self._y = y

    def move_by(self, dx, dy):
        """移动指定距离"""
        self._x += dx
        self._y += dy

    def distance_to(self, p2):
        return math.sqrt( (p2._x - self._x)**2 + (p2._y - self._y) ** 2 )

    def __str__(self):
        return '(%s, %s)' % (str(self._x), str(self._y))
    

def main():
    # clock = Clock(23, 58, 15)
    # for _ in range(600):
    #     clock.tick()
    #     clock.display()
    #     time.sleep(0.05)
    p1 = Point(3, 5)
    p2 = Point()

    print(p1, p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p2.distance_to(p1))

if __name__ == "__main__":
    main()

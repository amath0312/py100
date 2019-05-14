# -*- coding:utf8 -*-
import math
import random


def find_narcissistic(m):
    low = 10 ** (m - 1)
    high = 10 ** m
    for i in range(low, high, 1):
        val = 0
        for n in range(m):
            digit = (i // (10 ** (m - n - 1))) % 10
            val += digit ** m
            # print(digit, end = '')
        if val == i:
            print(i)


def find_perfect(high):
    for i in range(high):
        num = i + 1
        factors = []
        for x in range(1, num, 1):
            if num % x == 0:
                factors.append(x)

        print(num, factors)
        sum = 0
        for x in factors:
            sum += x
        if sum == num:
            print(num)


def chicken():
    for x in range(20):
        for y in range(33):
            if (5 * x + 3 * y + (100 - x - y) / 3) == 100 and (100 - x - y) % 3 == 0:
                print('公鸡%d, 母鸡%d, 小鸡%d' % (x, y, (100 - x - y)))


def fibonacci(count):
    a, b = 0, 1
    for i in range(count):
        a, b = b, (a + b)
        print(a)


def craps():
    money = 1000
    while money > 0:
        print('总资产：', money)
        while True:
            debt = int(input('请下注: '))
            if debt > 0 and debt <= money:
                break

        a = random.randint(1, 6)
        b = random.randint(1, 6)
        sum = a + b
        print('玩家摇出了%d点' % sum)

        if sum == 7 or sum == 11:
            print('玩家胜')
            money += debt
        elif sum == 2 or sum == 3 or sum == 12:
            print('玩家输')
            money -= debt
        else:
            is_finish = False
            target = sum
            while not is_finish:
                a = random.randint(1, 6)
                b = random.randint(1, 6)
                sum = a + b
                print('玩家摇出了%d点' % sum)
                if sum == target:
                    print('玩家胜')
                    money += debt
                    is_finish = True
                elif sum == 7:
                    print('玩家输')
                    money -= debt
                    is_finish = True
    print('你破产了...')

if __name__ == '__main__':
    find_narcissistic(3)
    find_perfect(10)
    chicken()
    fibonacci(20)

    craps()

# -*- coding:utf8 -*-

import sys
import os
import time
import random


def test_creator():
    f = [x + y for x in ['A', 'B', 'C', 'D'] for y in ['1', '2', '3']]
    print(f)
    print(sys.getsizeof(f))
    g = (x + y for x in ['A', 'B', 'C', 'D']
         for y in sorted(['1', '2', '3'], reverse=True))
    print(g)
    print(sys.getsizeof(g))
    for s in g:
        print(s)
    print()


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def run_loop(text):
    for _ in range(50):
        os.system('clear')
        text = text[1:] + text[0]
        print(text)
        time.sleep(0.2)


def verify_code(code_len):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    for _ in range(code_len):
        idx = random.randint(0, len(all_chars) - 1)
        code += all_chars[idx]

    return code


def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名
    :param filename: 文件名
    :param has_dot: 返回值是否包含点
    :return: 文件后缀名
    """
    idx = filename.rfind('.')
    if idx >= 0:
        suffix = filename[filename.rfind('.') + 1:]
    else:
        suffix = ''
    return '.' + suffix if has_dot else suffix


def max2(lst):
    sorted_lst = sorted(lst)
    return sorted_lst[-1], sorted_lst[-2]


def yanghui(rows):
    pre_row = None
    for row in range(rows):
        cur_row = [None] * (row + 1)
        # yh[row] = [None] * (row + 1)
        print('   ' * ((2 * rows - 1) - (2 * (row + 1) - 1)//2), end='')
        for col in range(row+1):
            if col == 0 or col == row:
                cur_row[col] = 1
            else:
                cur_row[col] = pre_row[col-1]+pre_row[col]
            print(str(cur_row[col]).center(3, ' '), end='   ')
        pre_row = cur_row
        print()

def display(balls):
    for i, ball in enumerate(balls):
        if i == len(balls)-1:
            print('|', end='')
        print('%02d'%ball, end=' ')
    print()


def random_choose_balls():
    red_balls = [n for n in range(1,34)]
    balls = random.sample(red_balls, 6)
    balls.sort()
    balls.append(random.randint(1,16))
    return balls

def lucky_man():
    """
    《幸运的基督徒》--约瑟夫环问题
    有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
    """
    persons = [True]*30
    counter = 0
    index = 0
    number = 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index = index % 30
    for alived in persons:
        print('基' if alived else '非', end=' ')
    print()

def display_board(board):
    os.system('clear')
    print('%s|%s|%s' % (board['TL'],board['TM'],board['TR']))
    print('-+-+-')
    print('%s|%s|%s' % (board['ML'],board['MM'],board['MR']))
    print('-+-+-')
    print('%s|%s|%s' % (board['BL'],board['BM'],board['BR']))
    print()

def board_game():
    init_board={
        'TL':' ', 'TM':' ', 'TR':' ',
        'ML':' ', 'BM':' ', 'BR':' ',
        'BL':' ', 'MM':' ', 'MR':' ',
    }
    while True:
        cur_board = init_board.copy()
        turn = 'x'
        display_board(cur_board)
        counter = 0
        while counter<9:
            move = input('it\'s %s turn: ' % turn)
            cur_board[move.upper()] = turn
            counter += 1
            if turn == 'x':
                turn = 'o'
            else:
                turn = 'x'
            display_board(cur_board)
        
        if input('continue?') == 'no':
            break
        

def main():
    # test_creator()
    # for n in fib(20):
    #     print(n, ',', end='')
    # print()
    # run_loop('北京欢迎你为你开天辟地…………')
    # print(verify_code(5))
    # print(get_suffix('abc.txt'))
    # print(get_suffix('abc'))
    # print(get_suffix('abc.txt', has_dot=True))
    # print(get_suffix('abc', has_dot=True))
    # print(get_suffix('.abc'))
    # print(get_suffix('.'))
    # print(get_suffix('abc.'))
    # print(max2([3,4,2,3,4,5,6,1,22,12,3]))
    # yanghui(9)
    # display(random_choose_balls())
    # lucky_man()
    board_game()

if __name__ == '__main__':
    main()

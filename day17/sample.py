
import time
from functools import wraps
from threading import Lock

# 装饰器


def record_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('in wrapper record_time')
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} => {result} (time={end-start:.8f})')
        print('out wrapper record_time')
        return result
    return wrapper


@record_time
def f1(*args):
    return sum(args)


def test_decorate1():
    print(f1(1, 2, 3, 4, 5))


# 自定义参数的装饰器
def record(output):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            output('in wrapper record')
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            output(f'{func.__name__} => {result} (time={end-start:.8f})')
            output('out wrapper record')
            return result
        return wrapper
    return decorate


@record(print)
def f2(*args):
    return sum(args)


def test_decorate2():
    print(f2(1, 2, 3, 4, 5))


# 装饰器类

class Record(object):
    def __init__(self, output):
        self._output = output

    def __call__(self, func):
        print(func)
        @wraps(func)
        def wrapper(*args, **kwargs):
            self._output('in wrapper Record')
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            self._output(f'{func.__name__} => {result} (time={end-start:.8f})')

            self._output('exit wrapper Record')
            return result
        return wrapper


@Record(print)
def f3(*args):
    return sum(args)


def test_decorate3():
    print(f3(1, 2, 3, 4, 5))


# 类装饰器2

class Record2(object):
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print('in wrapper Record2', *args)
        result = self._func(*args, **kwargs)
        print(f'{self._func.__name__}')
        print('exit wrapper Record2')
        return result


@Record2
def f4(*args):
    return sum(args)


def test_decorate4():
    print(f4(1, 2, 3, 4, 5))


# 单例模式

def singleton(cls):
    locker = Lock()
    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            with locker:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper


@singleton
class President(object):
    def __init__(self, name):
        self.name = name

    @record(print)
    @Record(print)
    @record_time
    def say(self, word):
        print('%s says %s' % (self.name, word))


def test_singleton():
    p1 = President('emmm')
    p2 = President('ahahahaha')
    print(p1.name)
    print(p2.name)
    print(p1 == p2)
    p1.say('im here')


def main():
    test_decorate1()
    test_decorate2()
    test_decorate3()
    test_decorate4()
    test_singleton()


if __name__ == '__main__':
    main()

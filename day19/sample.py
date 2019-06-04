

def fib(num):
    """生成器"""
    a,b=0,1
    for _ in range(num):
        a,b=b,a+b
        yield a

class Fib(object):
    """迭代器"""
    def __init__(self, num=10):
        self._a=0
        self._b=1
        self._idx=0
        self._num = 10
    
    def __iter__(self):
        self._idx=0
        self._a=0
        self._b=1
        return self

    def __next__(self):
        if self._idx < self._num :
            self._a, self._b = self._b, self._a+self._b
            self._idx += 1
            return self._a
        raise StopIteration()

if __name__ == '__main__':
    fib_iter = fib(5)
    for n in fib_iter:
        print(n)
    
    for i, n in enumerate(Fib()):
        print(i,n)
        if i > 20 :
            break
    
    fib_iter = Fib()
    for n in fib_iter:
        print('1 -', n)

    for n in fib_iter:
        print('2 -', n)
        
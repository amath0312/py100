
def factorial(num):
    """
    求阶乘
    
    :param num: 非负整数
    :return: num的阶乘
    """
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result

def sum(*args):
    """
    可变参数示例
    """
    val = 0
    for n in args:
        val += n
    return val

def foo():
    print('i am foo 1')

def foo():
    print('i am foo 2')

def test_mod():
    foo()
    from mod1 import foo
    foo()

    import mod1 as m1
    import mod2 as m2
    m1.foo()
    m2.foo()

def greatest_common_divisor(x, y):
    """
    最大公约数
    """
    x, y = (x, y) if x < y else (y, x)
    while x != y:
        y = y - x
        x, y = (x, y) if x < y else (y, x)
    return x

def least_common_multiple(x, y):
    return int(x * y / greatest_common_divisor(x, y))

def is_palindrome(num):
    """
    是否是回文数
    """
    
def main():
    # C(M, N)
    # m = int(input('m='))
    # n = int(input('n='))
    # print(factorial(m) // factorial(n) // factorial(m-n))

    # print(sum(1,2,3))
    
    # test_mod()

    print(greatest_common_divisor(60, 24))
    print(least_common_multiple(45, 30))

if __name__ == '__main__':
    main()
import math

def is_prime(num):
    """
    判断一个数是否为素数
    """
    if num == 1:
        return False
    for i in range(2,int(math.sqrt(num))):
        if num % i == 0:
            return False;
    
    return True

if __name__ == '__main__':
    num = 101
    print(is_prime(num))
    
    row = 5

    for i in range(row):
        print('*'*(i+1))

    for i in range(row):
        print(' '*(row-i-1)+'*'*(i+1))

    for i in range(row):
        print(' '*(row-i-1), end='')
        print('*'*(2*(i+1)-1))
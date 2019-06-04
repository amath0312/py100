import time
import threading

from concurrent.futures import ThreadPoolExecutor


class Account(object):
    """银行账户"""

    def __init__(self):
        self.balance = 0.0
        self.lock = threading.Lock()

    def deposit(self, money):
        # 通过锁保护临界资源
        with self.lock:
            new_balance = self.balance + money
            time.sleep(0.001)
            self.balance = new_balance
            return new_balance


class AddMoneyThread(threading.Thread):
    """自定义线程类"""

    def __init__(self, account, money):
        self.account = account
        self.money = money
        # 自定义线程的初始化方法中必须调用父类的初始化方法
        super().__init__()

    def run(self):
        # 线程启动之后要执行的操作
        self.account.deposit(self.money)

def main():
    """主函数"""
    account = Account()
    # 创建线程池
    pool = ThreadPoolExecutor(max_workers=10)
    futures = []
    for _ in range(100):
        # 创建线程的第1种方式
        # threading.Thread(
        #     target=account.deposit, args=(1, )
        # ).start()
        # 创建线程的第2种方式
        # AddMoneyThread(account, 1).start()
        # 创建线程的第3种方式
        # 调用线程池中的线程来执行特定的任务
        future = pool.submit(account.deposit, 1)
        futures.append(future)
    # 关闭线程池
    pool.shutdown()
    for future in futures:
        print(future.result())
    print(account.balance)

def yield_test(m,n):
    yield from range(m,n)

if __name__ == '__main__':
    main()
    for i in yield_test(3,5):
        print(i, end=' ')

    print()
    
    for i in yield_test(2,6):
        print(i, end=' ')

    
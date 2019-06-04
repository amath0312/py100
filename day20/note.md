# 并发编程

## 多线程

* Python中的列表、字典、集合都是线程安全的，所以使用线程而不是进程维护共享状态的代价相对较小
* 线程池

  ```python
  from concurrent.futures import ThreadPoolExecutor
  with ThreadPoolExecutor(max_workers=10) as pool:
        for _ in range(5):
            pool.submit(add_money, account)
            pool.submit(sub_money, account)
    ```

* 多个线程竞争一个资源 - 保护临界资源 - 锁（Lock/RLock）
* 多个线程竞争多个资源（线程数>资源数） - 信号量（Semaphore）
* 多个线程的调度 - 暂停线程执行/唤醒等待中的线程 - Condition

    ```python
    lock = threading.Lock()
    self.condition = threading.Condition(lock)
    # ...
    with self.condition:
        while money > self.balance:
            self.condition.wait()
        new_balance = self.balance - money
    # ...
    with self.condition:
        new_balance = self.balance + money
        sleep(0.001)
        self.balance = new_balance
        self.condition.notify_all()
    ```

## 多进程

> 多线程因为GIL的存在不能够发挥CPU的多核特性，对于计算密集型任务应该考虑使用多进程

```python
with concurrent.futures.ProcessPoolExecutor() as executor:
    for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
        print('%d is prime: %s' % (number, prime))
```

## 异步处理

> 当程序不需要真正的并发性或并行性，而是更多的依赖于异步处理和回调时，asyncio就是一种很好的选择。如果程序中有大量的等待与休眠时，也应该考虑asyncio，它很适合编写没有实时数据处理需求的Web应用服务器。

* asyncio模块、await和async关键字
* aiohttp


## 第三方库

> joblib、PyMP等

* 水平扩展：将单个节点变成多个节点
* 垂直扩展：增加单个节点的处理能力
* 消息队列：提供了排队、路由、可靠传输、安全等功能，如ActiveMQ、RabbitMQ等
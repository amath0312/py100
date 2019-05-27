# 函数的使用方式

* 函数是一等公民：
* filter和map的用法

  ```python
    items1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10))))
    items2 = [x ** 2 for x in range(1, 10) if x % 2]
  ```

* 参数类型
  * 位置参数

    ```python
    def power(m, n):
        pass
    ```

  * 默认参数

    ```python
    def power(m, n=3):
        pass
    ```

    * 必选参数在前，默认参数在后
    * 默认参数一定要指向不变对象

  * 可变参数

    ```python
    def power(*args):
        # args接收的是一个tuple
        pass
    power(1,2,3)

    tupleArray=(1,2,3)
    power(*tupleArray)
    ```

  * 关键字参数

    ```python
    def person(name, age, **kw):
        # kw接收到的是dict
        print('name:', name, 'age:', age, 'other:', kw)
    person('Jack', 24, gender='M')
    person('Jack', 24, **dictArray )
    ```

  * 命名关键字参数

    ```python
    # * 作为分隔符
    def person(name, age, *, city, job):
        pass

    # 前面定义了可变参数，不需要 * 分隔符
    def person2(name, age, *args, city, job):
        pass
    person2('jack',18,'some','args',city='bj',job='dev')
    ```

    * 命名关键字参数必须传入参数名，这和位置参数不同

  * 参数组合

    ```python
    def f1(a, b, c=0, *args, d, **kw):
        pass
    ```

    * 参数组合的顺序必须是：必选参数–>默认参数–>可变参数–>命名关键字参数–>关键字参数

* 参数的元信息
* 装饰器函数（使用装饰器和取消装饰器）
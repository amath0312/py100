
from random import randint


def test_generator():
    prices = {
        'AAPL': 191.88,
        'GOOG': 1186.96,
        'IBM': 149.24,
        'ORCL': 48.44,
        'ACN': 166.89,
        'FB': 208.09,
        'SYMC': 21.29
    }

    p2 = {k: v for k, v in prices.items() if v > 100}
    print(p2)

    keys = [k for k in prices] * 2
    print(keys)

    s = {k for k in keys}
    print(s)


def list_in_list():
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    courses = ['语文', '数学', '英语']
    scores = [[None] * len(courses) for _ in range(len(names))]
    for name in range(len(scores)):
        for course in range(len(scores[name])):
            scores[name][course] = randint(50, 100)
    print(scores)
    for name, score in enumerate(scores):
        for course, s in enumerate(scores[name]):
            print('%s.%s=%3d' % (names[name], courses[course], s), end='    ')
        print()


def test_heapq():
    """
    从列表中找出最大的或最小的N个元素
    堆结构(大根堆/小根堆)
    """
    import heapq
    list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
    list2 = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    print(heapq.nlargest(3, list1))
    print(heapq.nsmallest(2, list1))
    print(heapq.nlargest(3, list2, key=lambda x: x['price']))


def test_itertools():
    import itertools
    print([i for i in itertools.permutations('abcd')], end='\n=======\n')
    print([i for i in itertools.permutations('abcd', 2)], end='\n=======\n')

    print([i for i in itertools.combinations('abcd', 2)], end='\n=======\n')

    print([i for i in itertools.product('abcd')], end='\n=======\n')
    print([i for i in itertools.product('abc', '123')], end='\n=======\n')


def test_collections():
    import collections
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
        'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
        'look', 'into', 'my', 'eyes', "you're", 'under'
    ]
    counter = collections.Counter(words)
    print(counter)
    print(counter.most_common(3))
    print(counter.get('my'))
    print(counter['my'])


def fib(num, temp={}):
    """用递归计算Fibonacci数"""
    if num in (1, 2):
        return 1
    try:
        val = temp[num]
        print('find fib(%d) in temp' % num)
        return val
    except KeyError:
        temp[num] = fib(num - 1) + fib(num - 2)
        print('calc fib(%d)' % num)
        print('temp =', temp)
        return temp[num]


def max_subset(items):
    partial = [None] * len(items)  # items[i]为起点的子序列最大值
    overall = [None] * len(items)  # items[i:]子集中，子序列最大值
    pos = [None] * len(items)

    partial[-1] = items[-1]
    overall[-1] = items[-1]
    pos[-1] = (len(items) - 1, len(items) - 1)  # 子集合为items[start:end+1]

    for i in range(len(items) - 2, -1, -1):
        val = items[i]
        # 找出子集合最大值，并取出子集合
        start = i
        end = i
        partial_val = val + partial[i + 1]
        if val > partial_val:
            partial[i] = val
            end = i
        else:
            partial[i] = partial_val
            end = pos[i + 1][1]

        if partial[i] > overall[i + 1]:
            overall[i] = partial[i]
            start = i
        else:
            overall[i] = overall[i + 1]
            start, end = pos[i + 1]
        pos[i] = (start, end)

    return overall[0], pos[0]
    # 若不需要取出子集合，可用下面计算代替
    # partial[i] = max(val, val + partial[i + 1])
    # overall[i] = max(partial[i], overall[i + 1])
    # return overall[0]


def test_max_subset():
    samples = [
        '1 -2 3 5 -3 2',
        '0 -2 3 5 -1 2',
        '-9 -2 -3 -5 -3'
    ]
    for sample in samples:
        items = list(map(int, sample.split()))
        print(items, end=' ==> ')
        result = max_subset(items)
        print(result[0], end=' # ')
        print(items[result[1][0]:result[1][1] + 1])


def main():
    # test_generator()
    # list_in_list()
    # test_heapq()
    # test_itertools()
    # test_collections()

    # fib(3, {})
    # fib(5)
    # fib(5)

    test_max_subset()


if __name__ == "__main__":
    main()

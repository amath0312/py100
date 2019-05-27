from random import shuffle, randint


def sequence_search(items, key):
    '''顺序查找'''
    for idx, item in enumerate(items):
        if item == key:
            return idx
    return -1

def bin_search(sorted_items, key):
    '''二分查找'''
    start = 0
    end = len(sorted_items)-1
    while start <= end:
        mid = (start + end) // 2
        if key == sorted_items[mid]:
            return mid
        elif key > sorted_items[mid]:
            start = mid+1
        else:
            end = mid-1
    return -1

def main():
    for _ in range(100):
        items = [randint(-10, 10) for _ in range(10)]
        items = sorted(items)
        target = randint(-10,10)
        print('origin items:', items, ', target:', target)

        if target in items:
            expect_result = items.index(target)
        else:
            expect_result = -1
        print('expect:', expect_result)

        sequence_result = sequence_search(items, target)
        print('sequence_result:', sequence_result)
        
        bin_result = bin_search(items, target)
        print('bin_result:',bin_result)

        assert expect_result == sequence_result == bin_result == -1 \
             or items[sequence_result] == items[bin_result] == target


if __name__ == '__main__':
    main()

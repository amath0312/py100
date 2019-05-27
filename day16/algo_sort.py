import random


def bubble_sort(items, cmp=lambda x, y: x > y):
    """冒泡排序"""
    sorted_items = items[:]
    for i in range(len(sorted_items) - 1):
        for j in range(len(sorted_items) - 1 - i):
            if cmp(sorted_items[j], sorted_items[j + 1]):
                sorted_items[j +
                             1], sorted_items[j] = sorted_items[j], sorted_items[j + 1]

    return sorted_items


def select_sort(items, cmp=lambda x, y: x > y):
    """选择排序"""
    sorted_items = items[:]
    for i in range(len(sorted_items) - 1):
        min = sorted_items[i]
        idx = i
        for j in range(i, len(sorted_items)):
            if cmp(min, sorted_items[j]):
                min = sorted_items[j]
                idx = j
        sorted_items[i], sorted_items[idx] = sorted_items[idx], sorted_items[i]
    return sorted_items


def merge_sort(items, cmp=lambda x, y: x > y):
    """归并排序"""
    if(len(items)) < 2:
        return items[:]

    # if len(items) == 2:
    #     if cmp(items[0], items[1]):
    #         return [items[1], items[0]]
    #     else:
    #         return items[:]

    idx_mid = len(items) // 2
    left = items[:idx_mid]
    right = items[idx_mid:]
    sorted_left = merge_sort(left, cmp=cmp)
    sorted_right = merge_sort(right, cmp=cmp)

    # merge
    sorted_items = []
    left_idx = 0
    right_idx = 0
    for _ in range(len(items)):
        if cmp(sorted_left[left_idx], sorted_right[right_idx]):
            sorted_items.append(sorted_right[right_idx])
            right_idx += 1
        else:
            sorted_items.append(sorted_left[left_idx])
            left_idx += 1

        if left_idx >= len(sorted_left):
            sorted_items.extend(sorted_right[right_idx:])
            break
        elif right_idx >= len(sorted_right):
            sorted_items.extend(sorted_left[left_idx:])
            break

    return sorted_items


def quick_sort(items, cmp=lambda x, y: x > y):
    '''快速排序（分治法）'''
    if len(items) <= 1:
        return items[:]

    pivot_idx = len(items) // 2
    pivot = items[pivot_idx]
    less = []
    great = []
    for i, item in enumerate(items):
        if i != pivot_idx:
            if cmp(item, pivot):
                great.append(item)
            else:
                less.append(item)

    left = quick_sort(less)
    right = quick_sort(great)

    result = list(left)
    result.append(pivot)
    result.extend(right)
    return result


def quick_sort2(items, cmp=lambda x, y: x > y):
    '''快速排序（分治法） - 原地分隔'''
    sorted_items = items[:]
    _quick_sort2(sorted_items, 0, len(items) - 1, cmp)
    return sorted_items


def _quick_sort2(items, start, end, cmp):
    if start < end:
        pivot_idx = _partition(items, start, end, cmp)
        left = _quick_sort2(items, start, pivot_idx - 1, cmp)
        right = _quick_sort2(items, pivot_idx + 1, end, cmp)


def _partition(items, start, end, cmp):
    pivot = items[end]
    store_idx = start
    for i in range(start, end):
        if not cmp(items[i], pivot):
            items[store_idx], items[i] = items[i], items[store_idx]
            store_idx += 1
    items[store_idx], items[end] = items[end], items[store_idx]
    return store_idx


def main():
    for i in range(5):
        origin = [random.randint(-10, 10) for _ in range(3)]
        # random.shuffle(origin)
        # origin.reverse()
        print('origin:'.ljust(15), origin)

        expect_result = sorted(origin)
        print('expect:'.ljust(15), expect_result)

        bubble_result = bubble_sort(origin)
        print('bubble_sort:'.ljust(15), bubble_result)

        select_result = select_sort(origin)
        print('select_sort:'.ljust(15), select_result)

        merge_result = merge_sort(origin)
        print('merge_sort:'.ljust(15), merge_result)

        quick_result = quick_sort(origin)
        print('quick_sort:'.ljust(15), quick_result)

        quick2_result = quick_sort2(origin)
        print('quick_sort:'.ljust(15), quick_result)

        assert expect_result \
            == bubble_result \
            == select_result \
            == merge_result \
            == quick_result \
            == quick2_result
        print('=' * 15, 'ok\n')


if __name__ == "__main__":
    main()

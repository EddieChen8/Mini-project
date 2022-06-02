import random
import time


def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


#binary search uses divide and conquer!
# we will leverage this fact that our list is sorted


def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1
    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint

    elif l[midpoint] < target:
        return binary_search(l, target, midpoint + 1, high)
    else:
        return binary_search(l, target, low, midpoint - 1)


if __name__ == '__main__':

    # l = [1, 3, 5, 10, 21, 45, 90, 100]
    # target = 21
    # print(naive_search(l, target))
    # print(binary_search(l, target))

    length = 10000
    sorted_list = set()
    for i in range(length):
        sorted_list.add(random.randint(-3 * length, 3 * length))
    l = sorted(list(sorted_list))

    start = time.time()
    for target in l:
        naive_search(l, target)
    end = time.time()

    print('naive_search time:', (end - start) / length, 'seconds')

    start = time.time()
    for target in l:
        binary_search(l, target)
    end = time.time()

    print("binary_search time:", (end - start) / length, "seconds")

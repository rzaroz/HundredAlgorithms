import random
from random import shuffle

random.seed(43)

def heapify(lst, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and lst[left] > lst[largest]:
        largest = left

    if right < n and lst[right] > lst[largest]:
        largest = right

    if largest != i:
        lst[largest], lst[i] = lst[i], lst[largest]
        heapify(lst, n, largest)

def heap_sort(lst: list):
    n = len(lst)

    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i)


    for j in range(n - 1, 0, -1):
        lst[j], lst[0] = lst[0], lst[j]
        heapify(lst, j, 0)


test = [i for i in range(10)]
shuffle(test)

print("Before:")
print(test)
heap_sort(test)
print("After:")
print(test)
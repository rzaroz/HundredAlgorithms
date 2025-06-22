import random
from random import shuffle

random.seed(42)

def shell_sort(lst: list):
    n = len(lst)
    gap = n // 2

    while gap > 0:

        for i in range(gap, n):
            temp = lst[i]
            j = i

            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap

            lst[j] = temp

        gap //= 2


test_lst = [i for i in range(100)]
shuffle(test_lst)

print("Before:")
print(test_lst)
print("After:")
shell_sort(test_lst)
print(test_lst)
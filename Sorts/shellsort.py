import time
import random
from random import shuffle

start_time = time.perf_counter()


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
done = time.perf_counter() - start_time
print(f"Code execution time: {done:.6f} seconds")
print(test_lst)
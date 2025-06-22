import time
import random
from random import shuffle
start_time = time.perf_counter()

def insertion_sort(lst: list):

    for i in range(1, len(lst)):

        for j, n in enumerate(lst[:i]):

            if lst[i] < n:
                lst[i], lst[j] = lst[j], lst[i]

    return lst

test_lst = [i for i in range(100)]
shuffle(test_lst)

print("Before:")
print(test_lst)
print("After:")
insertion_sort(test_lst)
done = time.perf_counter() - start_time
print(f"Code execution time: {done:.6f} seconds")
print(test_lst)
import time
from random import shuffle

start_time = time.perf_counter()
def counting_sort_radix(lst, exp):
    n = len(lst)
    count = [0] * 10
    output = [0] * n

    for number in lst:
        index = (number // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for j in range(n - 1, -1, -1):
        index = (lst[j] // exp) % 10
        output[count[index] - 1] = lst[j]

        count[index] -= 1


    for k in range(n):
        lst[k] = output[k]


def radix_sort(lst):
    max_num = max(lst)

    exp = 1
    while max_num // exp > 0:
        counting_sort_radix(lst, exp)
        exp *= 10


test_lst = [i for i in range(10)]
shuffle(test_lst)

print(test_lst)
radix_sort(test_lst)
end_time = time.perf_counter()

elapsed_time = end_time - start_time
print(f"Code execution time: {elapsed_time:.6f} seconds")
print(test_lst)
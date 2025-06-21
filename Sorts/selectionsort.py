import time
import numpy as np

start_time = time.perf_counter()
def selection_sort(lst: list):
    lst_len = len(lst)

    for i in range(lst_len - 1):

        min_ = i
        for j in range(i+1, lst_len):
            if lst[min_] > lst[j]:
                min_ = j

        lst[i], lst[min_] = lst[min_], lst[i]


    return lst

test_lst = np.random.randn(10) * 100
test_lst = test_lst.tolist()
print(test_lst)
result = selection_sort(test_lst)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Code execution time: {elapsed_time:.6f} seconds")
print(result)
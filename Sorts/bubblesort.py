import copy
import numpy as np

def bubble_sort(lst):
    result = copy.deepcopy(lst)
    n = len(result)

    # 1- First loop on main list
    for i in range(n):
        # 2- loop on main list again but to not sorted parts
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result

test_lst = np.random.randn(10) * 10
test_lst = test_lst.tolist()

result_ = bubble_sort(test_lst)

print("Original list:")
print(test_lst)
print("Bubble sort:")
print(result_)

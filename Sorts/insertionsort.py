import numpy as np

def insertion_sort(lst: list):

    for i in range(1, len(lst)):

        for j, n in enumerate(lst[:i]):

            if lst[i] < n:
                lst[i], lst[j] = lst[j], lst[i]

    return lst

test_lst = np.random.randn(10) * 10
test_lst = test_lst.tolist()

print("Before:")
print(test_lst)
result = insertion_sort(test_lst)
print("After:")
print(result)
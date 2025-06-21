import random
from random import shuffle

random.seed(43)

def counting_sort(lst):
    min_num = min(lst)
    max_num = max(lst)
    length = max_num - min_num + 1
    output = [0] * len(lst)
    count = [0] * length

    for number in lst:
        count[number - min_num] += 1

    for i in range(1, length):
        count[i] += count[i - 1]


    for j in range(len(lst) - 1, -1, -1):
        output[count[lst[j] - min_num] - 1] = lst[j]
        count[lst[j] - min_num] -= 1

    return output

test_lst = [i for i in range(10)]
shuffle(test_lst)

print(test_lst)
result = counting_sort(test_lst)
print(result)


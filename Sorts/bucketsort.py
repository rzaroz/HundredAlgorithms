import random
from random import shuffle

random.seed(43)

def bucket_sort(lst: list, bucket_size: int):
    min_element = min(lst)
    max_element = max(lst)
    bucket_range = (max_element - min_element) / 10
    buckets = [[] for _ in range(bucket_size)]
    result = []

    for number in lst:
        index = round((abs(number) - min_element) / bucket_range)
        if index != 0:
            index = index - 1
        buckets[index].append(number)

    for bucket in buckets:
        bucket.sort()
        result.extend(bucket)

    return result

test_lst = [i / 10 for i in range(20)]
shuffle(test_lst)
result_sorted = bucket_sort(test_lst, len(test_lst))
print(test_lst)
print(result_sorted)
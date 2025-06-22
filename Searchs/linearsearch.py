import random

random.seed(42)

def linear_search(lst: list, target):
    position = None

    for i, number in enumerate(lst):
        if target == number:
            position = i
            break

    return position


test_lst = [num for num in range(100)]
random.shuffle(test_lst)
result = linear_search(test_lst, 71)
print(test_lst[result])

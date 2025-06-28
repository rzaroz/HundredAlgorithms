import math

def jump_search(lst: list, target):
    n = len(lst)
    step = int(math.sqrt(n))
    prev = 0

    while step < n and lst[step - 1] < target:
        prev = step
        step += int(math.sqrt(n))

    if prev >= n:
        return -1

    for i in range(prev, min(step, n)):
        if lst[i] == target:
            return i

    return -1


test_lst = [i + 1 for i in range(101)]
result_ = jump_search(test_lst, 45)
print(result_)
from binraysearch import binary_search

def exponential_search(lst: list, target):
    if target == lst[0]:
        return 0

    n= len(lst)
    step = 1

    while step < n and lst[step] < target:
        step *= 2

    return binary_search(arr=lst, target=target, low=step//2, high=min(step, n - 1))


test_lst = [i+1 for i in range(100)]
result = exponential_search(test_lst, 32 )
print(result)
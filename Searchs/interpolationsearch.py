def interpolation_search(lst: list, target):
    low = 0
    high = len(lst) - 1

    while low <= high and lst[low] <= target <= lst[high]:
        pos = low + ((target - lst[low]) * (high - low)) // (lst[high] - lst[low])

        if lst[pos] == target:
            return pos
        elif lst[pos] < target:
            high = pos - 1
        else:
            low = pos + 1

    return -1


test_lst = [i * 15 for i in range(1, 100)]
result = interpolation_search(test_lst, 75)

if result != -1:
    print(f"Value found in index {result}. ({test_lst[result]})")
else:
    print("Not found!")
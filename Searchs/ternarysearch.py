
def ternary_search(arr, x, left, right):

    if left < right:

        middle_first = left + (right - left) // 3
        middle_second = right - (right - left) // 3

        if x == arr[middle_first]:
            return middle_first

        if x == arr[middle_second]:
            return middle_second

        if x < arr[middle_first]:
            return ternary_search(arr, x, left, middle_first - 1)
        elif x > arr[middle_second]:
            return ternary_search(arr, x, middle_second + 1, right)
        else:
            return ternary_search(arr, x, middle_first+1, middle_second-1)

    return -1

test_lst = [i * 15 for i in range(1, 100)]
result = ternary_search(test_lst, 405, 0, len(test_lst) - 1)

if result != -1:
    print(f"Value found in index {result}. ({test_lst[result]})")
else:
    print("Not found!")
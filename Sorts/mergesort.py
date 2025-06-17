import random

def merge(left: list, right: list):
    result = []
    left_counter = 0
    right_counter = 0

    while left_counter < len(left) and right_counter < len(right):

        if left[left_counter] < right[right_counter]:
            result.append(left[left_counter])
            left_counter += 1
        else:
            result.append(right[right_counter])
            right_counter += 1


    result += left[left_counter:]
    result += right[right_counter:]

    return result

def merge_sort(lst: list):

    if len(lst) == 1:
        return lst
    else:
        middle = len(lst) // 2
        left = merge_sort(lst[:middle])
        right = merge_sort(lst[middle:])

    return merge(left, right)


test_list = [i for i in range(10)]
random.shuffle(test_list)

print("Before:")
print(test_list)
print("After:")
print(merge_sort(test_list))
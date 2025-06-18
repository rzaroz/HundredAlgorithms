from random import shuffle

def quick_sort(lst: list, low, high):
    if low < high:
        pivot = low
        i = low
        j = high

        while i < j:

            while lst[i] <= lst[pivot] and i < high:
                i+=1

            while lst[j] > lst[pivot]:
                j -= 1


            if i < j:
                lst[i], lst[j] = lst[j], lst[i]


        lst[j], lst[pivot] = lst[pivot], lst[j]

        quick_sort(lst, low, j-1)
        quick_sort(lst, j+1, high)

    return lst

test_list = [i for i in range(0, 10)]
shuffle(test_list)

print(test_list)
print(quick_sort(test_list, 0, len(test_list)-1))
def binary_search(arr, target, low=0, high=None):

    if not high:
        high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    test = [i for i in range(120)]
    target_ = 99
    result = binary_search(test, target_)
    print(target_)


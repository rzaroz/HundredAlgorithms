def fibonachi_search(arr, x):
    n = len(arr)
    a = 0
    b = 1
    c = 1
    while c < n:
        a = b
        b = c
        c = a + b
    offset = -1
    while c > 1:
        i = min(offset + a, n - 1)

        if arr[i] < x:
            c = b
            b = a
            a = c - b
            offset = i
        elif arr[i] > x:
            c = a
            b = b - a
            a = c - b
        else:
            return i
    if b and (offset + 1) < n and arr[offset + 1] == x:
        return offset + 1

    return -1



lst = [i for i in range(10)]
target = 23
result = fibonachi_search(lst, target)
print(result)
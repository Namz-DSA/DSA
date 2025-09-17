def lastOccurence(arr, target):
    l, r = 0, len(arr) - 1

    res = -1

    while l <= r:
        mid = (l+r)//2

        if arr[mid] == target:
            res = mid
            l = mid + 1
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return res

print(lastOccurence([1, 3, 3, 3, 5, 7], 3))
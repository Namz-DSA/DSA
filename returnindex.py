def findIndexBinarySearch(arr, target):
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

print(findIndexBinarySearch([1, 3, 5, 7, 9, 11], 4))
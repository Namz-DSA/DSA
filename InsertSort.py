def InsertSort(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
    return arr

print(InsertSort([5, 2, 9, 1]))
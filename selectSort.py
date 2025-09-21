def selectSort(arr):
    n = len(arr)
    for i in range(0, n-1):
        min_idx = i
        for j in range(i+1, n):
           if arr[j] < arr[min_idx]:
               min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


print(selectSort([5, 2, 9, 1, 5]))
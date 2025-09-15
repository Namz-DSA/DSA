def issorted(arr):
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            return False
    return True
    
print(issorted([3,2,3,4,5]))
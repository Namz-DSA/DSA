def findIndexBinarySearchRecursive(arr, target, l = 0, r = None):
    if r == None:
        r = len(arr) - 1
    
    if l > r:
        return - 1
    
    mid = (l+r)//2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return findIndexBinarySearchRecursive(arr, target, mid+1, r)
    else:
        return findIndexBinarySearchRecursive(arr, target, l, r = mid-1)


print(findIndexBinarySearchRecursive([1, 3, 5, 7, 9, 11], 7)) 
print(findIndexBinarySearchRecursive([1, 3, 5, 7, 9, 11], 4)) 
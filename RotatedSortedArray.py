def RotatedSortedArray(arr, target):
    l, r = 0, len(arr)-1

    while l <= r:
        mid = (l+r)//2

        if arr[mid] == target:
            return mid
        
        if arr[l] <= arr[mid]:
            if arr[l] <= target <= arr[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        else:
            if arr[mid] < target <= arr[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1

print(RotatedSortedArray([4, 5, 6, 7, 0, 1, 2], 0)) 
print(RotatedSortedArray([4, 5, 6, 7, 0, 1, 2], 3))  
print(RotatedSortedArray([6,7,1,2,3,4,5], 4))
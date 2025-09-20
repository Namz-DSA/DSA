def MaxDifference(arr):
    min_so_far = float('inf')
    max_diff = -1

    for i in range(len(arr)):
        max_diff = max(max_diff, arr[i]-min_so_far)
        min_so_far = min(min_so_far, arr[i])
    
    return max_diff

print(MaxDifference([7, 1, 5, 3, 6, 4]))
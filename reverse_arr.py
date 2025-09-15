def reverse_arr(arr):
    l, r = 0, len(arr)-1

    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    return arr

print(reverse_arr([1,2,3,4,5]))
def min_array(arr):
    min_arr = arr[0]

    for a in arr:
        if a < min_arr:
            min_arr = a
    return min_arr

print(min_array([4,2,7,1,9]))
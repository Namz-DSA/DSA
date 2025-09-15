def max_array(arr):
    max_arr = arr[0]
    for el in arr:
        if el > max_arr:
            max_arr = el
    return max_arr
print(max_array([1,5,3,9,2]))
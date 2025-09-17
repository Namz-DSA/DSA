def KthLargestQuickSelect(arr, k):
    if not arr or k <= 0:
        return None
    
    pivot = arr[-1]

    greater = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]
    smaller = [x for x in arr if x < pivot]

    if k <= len(greater):
        return KthLargestQuickSelect(greater, k)
    elif k <= len(greater) + len(equal):
        return pivot
    else:
        return KthLargestQuickSelect(smaller, k-len(greater)-len(equal))


print(KthLargestQuickSelect([7, 5, 2, 9, 1, 8], 1))
print(KthLargestQuickSelect([7, 5, 2, 9, 1, 8], 2))
print(KthLargestQuickSelect([7, 5, 2, 9, 1, 8], 3))
print(KthLargestQuickSelect([7, 5, 2, 9, 1, 8], 6))
print(KthLargestQuickSelect([9,9,9], 4))
def secondLargest(l):
    first_max = second_max = float('-inf')
    for num in l:
            if num > first_max:
                second_max = first_max
                first_max = num
            elif num > second_max and num != first_max:
                 second_max = num
    return second_max if second_max != float('-inf') else None

print(secondLargest([10,20,4,45,90]))
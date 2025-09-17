def secondLargest(arr):
   max1 = float('-inf')
   max2 = float('-inf')

   for num in arr:
      if num > max1:
         max2 = max1
         max1 = num
      elif num > max2 and num != max1:
         max2 = num
   return max2 if max2 != float('-inf') else None

# print(secondLargest([7, 5, 2, 9, 1])) # 7
# print(secondLargest([9,9,9])) # None
print(secondLargest([-5, -2, -10, -3])) # -3
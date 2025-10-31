def RotateArray(nums, k):
    if k == 0 or len(nums) <= 1:
        return nums
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums

print(RotateArray([1,2,3,4,5,6,7],3))
print(RotateArray([1,2,3,4,5],7))
print(RotateArray([1],0))
def prefixSum(nums):
    prefix = [0] * len(nums)
    prefix[0] = nums[0]

    for i in range(1,len(nums)):
        prefix[i] = prefix[i-1] + nums[i]
    return prefix

print(prefixSum([1,2,3,4,5]))


def prefixSum(nums):
    prefix = []
    running_sum = 0

    for num in nums:
        running_sum += num
        prefix.append(running_sum)
    return prefix

print(prefixSum([1,2,3,4,5]))
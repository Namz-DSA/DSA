def checkSubArraySum(nums,K):
    running_sum = 0
    seen = set()

    for num in nums:
        running_sum += num
        if running_sum == K:
            return True
        if running_sum-K in seen:
            return True
        seen.add(running_sum)
    return False

print(checkSubArraySum([5,7,3,2],12))
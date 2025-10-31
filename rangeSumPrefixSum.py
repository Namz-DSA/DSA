def rangeSum(nums,queries):
    #do prefix sum first

    prefix = []

    running_sum = 0

    for num in nums:
        running_sum += num
        prefix.append(running_sum)
    
    total = []
    
    for (l,r) in queries:
        if l == 0:
            total.append(prefix[r])
        else:
            total.append(prefix[r] - prefix[l-1])
    print(total)


rangeSum([2,4,6,8,10],[(0,2),(1,3),(2,4)])
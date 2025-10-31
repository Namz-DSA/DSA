def searchRange(nums, target):
        def findFirst(nums,target):
            l, r = 0 , len(nums)-1
            res = -1

            while l <= r:
                mid = (l + r)//2

                if nums[mid] == target:
                    res = mid
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return res
        def findLast(nums,target):
            l, r = 0 , len(nums)-1
            res = -1

            while l <= r:
                mid = (l + r)//2

                if nums[mid] == target:
                    res = mid
                    l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return res
        return [findFirst(nums,target), findLast(nums,target)]
print(searchRange([1, 3, 3, 3, 5, 7], 3))
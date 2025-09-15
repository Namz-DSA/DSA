from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        arr = []

        while l < r:
            if abs(nums[l]) < nums[r]:
                r -= 1
            elif abs(nums[l]) > nums[r]:
                l += 1
            elif abs(nums[l]) == nums[r]:
                arr.append(nums[r])
                l+= 1
                r-= 1
            
        return max(arr, default = -1)


s = Solution()
print(s.findMaxK([-17,48,12,-28,19,-33,13,-39,-30,-30]))
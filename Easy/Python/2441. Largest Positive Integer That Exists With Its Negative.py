class Solution(object):
    def findMaxK(self, nums):
        nums.sort()
        start = 0
        end = len(nums) - 1
        this_max = -1
        if 0 < nums[start]:
            return this_max
        
        while start < end:
            if nums[start] + nums[end] == 0:
                this_max = nums[end]
                break
            elif abs(nums[start]) < nums[end]:
                end -= 1
            else:
                start += 1
        
        return this_max

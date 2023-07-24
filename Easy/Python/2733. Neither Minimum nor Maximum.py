class Solution(object):
    def findNonMinOrMax(self, nums):
        if len(nums) <= 2:
            return -1
        nums.sort()
        return nums[1]

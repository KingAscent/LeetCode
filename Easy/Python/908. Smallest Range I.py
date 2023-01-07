class Solution(object):
    def smallestRangeI(self, nums, k):
        nums.sort()
        if len(nums) == 1 or nums[len(nums) - 1] - k <= nums[0] + k:
            return 0
        
        return nums[len(nums) - 1] - nums[0] - k * 2

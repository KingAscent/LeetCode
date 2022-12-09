class Solution(object):
    def maxProductDifference(self, nums):
        nums.sort()
        length = len(nums) - 1
        return (nums[length] * nums[length - 1]) - (nums[0] * nums[1])

class Solution(object):
    def maxProduct(self, nums):
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1
        
        # Pythonic one liner
        # return (sorted(nums)[-1] - 1) * (sorted(nums)[-2] - 1)

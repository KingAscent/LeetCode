class Solution(object):
    def sumOfSquares(self, nums):
        this_sum = 0

        for i in range(len(nums)):
            if len(nums) % (i + 1) == 0:
                this_sum += nums[i] * nums[i]
        
        return this_sum

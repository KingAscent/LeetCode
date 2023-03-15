class Solution(object):
    def minStartValue(self, nums):
        this_sum = 0

        for i in range(len(nums)):
            this_sum += nums[i]
            nums[i] = this_sum
        
        nums.sort()

        if 0 < nums[0]:
            return 1
        else:
            return abs(nums[0]) + 1

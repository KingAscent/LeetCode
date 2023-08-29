class Solution(object):
    def maxAscendingSum(self, nums):
        this_sum = nums[0]
        max_sum = this_sum

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                this_sum += nums[i]
            else:
                max_sum = max(max_sum, this_sum)
                this_sum = nums[i]
        
        return this_sum if max_sum < this_sum else max_sum
        

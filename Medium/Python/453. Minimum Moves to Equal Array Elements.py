class Solution(object):
    def minMoves(self, nums):
        my_sum = 0
        minimum = nums[0]

        for i in range(len(nums)):
            if nums[i] < minimum:
                minimum = nums[i]
            my_sum += nums[i]
        
        return my_sum - (len(nums) * minimum)

class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        slices = 0
        prev = 0

        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                prev += 1
                slices += prev
            else:
                prev = 0
        
        return slices

class Solution(object):
    def leftRigthDifference(self, nums):
        left = 0
        right = 0

        for n in nums:
            right += n
        
        for i in range(len(nums)):
            left += nums[i]
            right -= nums[i]
            nums[i] = abs((left - nums[i]) - right)

        return nums

class Solution(object):
    def findMiddleIndex(self, nums):
        right = 0
        left = 0

        for i in range(len(nums)):
            right += nums[i]
        for i in range(len(nums)):
            right -= nums[i]
            if left == right:
                return i
            left += nums[i]
        
        return -1

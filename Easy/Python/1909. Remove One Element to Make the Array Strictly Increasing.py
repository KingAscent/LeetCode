class Solution(object):
    def canBeIncreasing(self, nums):
        count = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                count += 1
                if 1 < count:
                    return False
                if 1 < i and nums[i] <= nums[i - 2]:
                    nums[i] = nums[i - 1]
        
        return True

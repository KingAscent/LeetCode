class Solution(object):
    def pivotIndex(self, nums):
        pivot = -1
        left = 0
        total = 0

        for n in nums:
            total += n
        
        for i in range(len(nums)):
            if left * 2 == total - nums[i]:
                pivot = i
                break
            else:
                left += nums[i]
        
        return pivot

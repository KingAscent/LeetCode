class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) < 3:
            return len(nums)
        
        i = 2
        for j in range(i, len(nums)):
            if nums[i - 2] != nums[j]:
                nums[i] = nums[j]
                i += 1
        
        return i

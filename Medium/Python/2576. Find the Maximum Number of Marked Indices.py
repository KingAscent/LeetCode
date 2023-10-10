class Solution(object):
    def maxNumOfMarkedIndices(self, nums):
        i = 0
        j = (len(nums) + 1) / 2
        nums.sort()

        while j < len(nums):
            if 2 * nums[i] <= nums[j]:
                i += 1
            j += 1
        
        return 2 * i

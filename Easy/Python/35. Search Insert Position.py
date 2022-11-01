class Solution(object):
    def searchInsert(self, nums, target):
        # Go over the array looking for the target, or when the
        # element is larger than the target number
        for i in range(len(nums)):
            if(nums[i] == target or target < nums[i]):
                return i
        
        # The target was not found and is larger than all
        # elements in the array
        return len(nums)

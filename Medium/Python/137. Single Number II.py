class Solution(object):
    def singleNumber(self, nums):
        # Filter out lists of length 1
        if(len(nums) == 1):
            return nums[0]
        
        # Sort the list and find the integer that does not match
        # the integers to the left and right of it
        nums.sort()
        if(nums[0] != nums[1]): # If the 1st integer does not match the 2nd
            return nums[0]
        for i in range(1, len(nums) - 1):
            if(nums[i - 1] < nums[i] < nums[i + 1]):
                return nums[i]
        
        # Return the last number in the list
        return nums[len(nums) - 1]

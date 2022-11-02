class Solution(object):
    def numIdenticalPairs(self, nums):
        # Keep track of number of good pairs
        count = 0
        
        # Go over the array using a nested for loop, comparing
        # each element looking for good pairs
        for i in range(len(nums) - 1):
            for j in range(1, len(nums)):
                if (i < j) and (nums[i] == nums[j]):
                    count += 1
        
        # Return the number of good pairs
        return count

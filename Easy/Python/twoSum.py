class Solution(object):
    def twoSum(self, nums, target):
        # Array that would be returned
        solution = []
        
        # Check each index's integer and see if they
        # add up to the target, and if so, add their\
        # indexes to the solution array
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if((nums[i] + nums[j]) == target):
                    solution=[i, j]
        
        return solution

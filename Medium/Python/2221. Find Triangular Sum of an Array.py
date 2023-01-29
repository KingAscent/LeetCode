class Solution(object):
    def triangularSum(self, nums):
        # Initialize a variable to contain number of elements
        tSum = len(nums)

        while tSum != 1:
            # Run until every number has been added into the 0th index
            for i in range(tSum - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
            tSum -= 1
        
        # Return the 0th index
        return nums[0]

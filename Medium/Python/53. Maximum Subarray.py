class Solution(object):
    def maxSubArray(self, nums):
        # Initialize 2 variables to keep track of the sum
        maxSum = nums[0]
        tempSum = maxSum

        # Use a for loop to see what the largest subarray is
        for i in range(1, len(nums)):
            tempSum = max(tempSum + nums[i], nums[i])
            maxSum = max(tempSum, maxSum)
        
        # Return the largest subarray sum
        return maxSum

class Solution(object):
    def jump(self, nums):
        # Initial values
        maximum = 0
        jump = 0
        count = 0

        # Use a foor loop to check how far we can jump
        for i in range(len(nums) - 1):
            maximum = max(maximum, i + nums[i])
            if jump == i:
                jump = maximum
                count += 1
        
        # Return the number of jumps taken
        return count

class Solution(object):
    def canJump(self, nums):
        # Initialize a jump value
        jump = 0

        # Use a for loop to check how far each index allows us to jump
        # And see if we are able to jump over each zero
        for i in range(len(nums)):
            if jump < i:
                # We cannot jump over the zero, return false
                return False
            jump = max(jump, i + nums[i])

        # All zeros are able to be jumped over
        return True

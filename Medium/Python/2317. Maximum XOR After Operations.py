class Solution(object):
    def maximumXOR(self, nums):
        xor = 0

        for i in range(len(nums)):
            xor |= nums[i]

        return xor

class Solution(object):
    def maximumStrongPairXor(self, nums):
        xor = 0
        nums.sort()

        for x in nums:
            for y in nums:
                xor = max(xor, x ^ y) if abs(x - y) <= min(x, y) else xor
        
        return xor

class Solution(object):
    def minBitFlips(self, start, goal):
        xor = start ^ goal # This will give us the xor of start and goal
        count = 0

        while xor != 0:
            if (xor & 1) == 1:
                count += 1
            xor >>= 1 # Shift right
        
        return count
        

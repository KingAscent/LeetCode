class Solution(object):
    def largestAltitude(self, gain):
        high = 0
        point = 0

        for i in range(len(gain)):
            point += gain[i]
            high = max(high, point)
        
        return high

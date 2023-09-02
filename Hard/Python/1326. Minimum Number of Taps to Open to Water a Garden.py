class Solution(object):
    def minTaps(self, n, ranges):
        this_range = [0] * (n + 1)

        for i in range(len(ranges)):
            left = max(0, i - ranges[i])
            right = min(n, i + ranges[i])
            this_range[left] = max(this_range[left], right)
        
        end, maxRange, taps, i = 0, 0, 0, 0

        while end < n:
            while i <= end:
                maxRange = max(maxRange, this_range[i])
                i += 1
            
            if maxRange <= end:
                return -1 # Can't water the garden
            end = maxRange
            taps += 1
        
        return taps

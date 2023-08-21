class Solution(object):
    def maxPower(self, s):
        maximum = 0
        n = 0

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                n += 1
            else:
                n = 0
            maximum = max(maximum, n)
        
        return max(maximum, n) + 1

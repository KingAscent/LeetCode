class Solution(object):
    def countGoodSubstrings(self, s):
        if len(s) <= 2:
            return 0
        count = 0

        for i in range(len(s) - 2):
            if s[i] != s[i + 1] and s[i + 1] != s[i + 2] and s[i + 2] != s[i]:
                count += 1
        
        return count

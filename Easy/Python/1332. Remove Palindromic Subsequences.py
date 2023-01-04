class Solution(object):
    def removePalindromeSub(self, s):
        if len(s) == 0:
            return 0
        
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return 2
            else:
                i += 1
                j -= 1

        return 1

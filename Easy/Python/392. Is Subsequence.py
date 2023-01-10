class Solution(object):
    def isSubsequence(self, s, t):
        if len(s) == 0:
            return True
        if len(t) < len(s):
            return False
        
        sub = 0

        for i in range(len(t)):
            if s[sub] == t[i]:
                sub += 1
                if sub == len(s):
                    return True

        return False

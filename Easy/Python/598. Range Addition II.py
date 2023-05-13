class Solution(object):
    def maxCount(self, m, n, ops):
        r = m
        c = n

        for i in ops:
            r = min(r, i[0])
            c = min(c, i[1])
        
        return r * c

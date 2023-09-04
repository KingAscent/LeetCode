class Solution(object):
    def findContentChildren(self, g, s):
        count = 0
        i = 0
        g.sort()
        s.sort()

        for j in range(len(g)):
            while i < len(s) and s[i] < g[j]:
                i += 1
            if i == len(s):
                break
            i += 1
            count += 1
        
        return count

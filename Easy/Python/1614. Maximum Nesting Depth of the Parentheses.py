class Solution(object):
    def maxDepth(self, s):
        depth = 0
        open_paren = 0

        for i in range(len(s)):
            if s[i] == '(':
                open_paren += 1
                depth = max(depth, open_paren)
            if s[i] = ')':
                open_paren -= 1
        
        return depth

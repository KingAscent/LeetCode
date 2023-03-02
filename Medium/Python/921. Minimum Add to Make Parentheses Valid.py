class Solution(object):
    def minAddToMakeValid(self, s):
        start = 0
        end = 0

        for i in range(len(s)):
            if s[i] == '(':
                end += 1
            else:
                if end != 0:
                    end -= 1
                else:
                    start += 1
        
        return start + end

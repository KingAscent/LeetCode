class Solution(object):
    def partitionString(self, s):
        start = 0
        end = 0
        count = 0

        while end < len(s):
            if s[end] + "" in s[start:end]:
                count += 1
                start = end
            end += 1
        
        if s[end - 1] + "" in s[start:end]:
            count += 1
        
        return count

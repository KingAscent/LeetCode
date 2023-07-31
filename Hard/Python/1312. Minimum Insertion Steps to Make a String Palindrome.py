class Solution(object):
    def minInsertions(self, s):
        n = len(s)
        minimum = [0] * n

        for i in range(n - 1, -1, -1):
            prev = 0
            for j in range(i, n):
                temp = minimum[j]
                if s[i] == s[j]:
                    minimum[j] = prev
                else:
                    minimum[j] = min(minimum[j], minimum[j - 1]) + 1
                prev = temp
        
        return minimum[n - 1]

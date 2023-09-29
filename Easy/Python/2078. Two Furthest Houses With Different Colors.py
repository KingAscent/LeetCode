class Solution(object):
    def maxDistance(self, colors):
        n = len(colors)
        i = 0
        j = n - 1

        while colors[0] == colors[j]:
            j -= 1
        while colors[n - 1] == colors[i]:
            i += 1
        
        return max(j, n - i - 1)

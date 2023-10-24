class Solution(object):
    def shortestToChar(self, s, c):
        length = len(s)
        dist = [length] * length

        for i in range(length):
            if s[i] == c:
                for j in range(length):
                    dist[j] = min(dist[j], abs(i - j))
        
        return dist

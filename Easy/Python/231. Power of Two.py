class Solution(object):
    def isPowerOfTwo(self, n):
        return 0 < n and (n & n - 1) == 0

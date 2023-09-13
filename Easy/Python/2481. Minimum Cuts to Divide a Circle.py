class Solution(object):
    def numberOfCuts(self, n):
        return 0 if n == 1 else n / 2 if n % 2 == 0 else n

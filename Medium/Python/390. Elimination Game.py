class Solution(object):
    def lastRemaining(self, n):
        last = 1
        if n == 1:
            return last
        else:
            temp = self.lastRemaining(n / 2)
            last = 2 * ((n / 2) - temp + 1)
        return last

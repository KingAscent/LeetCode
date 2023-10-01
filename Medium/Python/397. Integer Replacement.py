class Solution(object):
    def integerReplacement(self, n):
        count = self.checkCount(n)

        return count
    
    def checkCount(self, n):
        if n == 1:
            return 0
        elif n % 2 == 0:
            return 1 + self.checkCount(n / 2)
        else:
            return 1 + min(self.checkCount(n + 1), self.checkCount(n - 1))

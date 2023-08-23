class Solution(object):
    def arrangeCoins(self, n):
        count = 0
        row = 1

        while 0 < n:
            n -= row
            row += 1
            if 0 <= n:
                count += 1
        
        return count

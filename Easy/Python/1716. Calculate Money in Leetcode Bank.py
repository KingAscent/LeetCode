class Solution(object):
    def totalMoney(self, n):
        mon = n / 7 # Get number of full weeks
        bank = 0

        # Money from full weeks
        for i in range(1, mon + 1, 1):
            bank += 7 * (i + 3)
        
        # Money for leftover days
        for i in range(7 * mon, n, 1):
            mon += 1
            bank += mon
        
        return bank

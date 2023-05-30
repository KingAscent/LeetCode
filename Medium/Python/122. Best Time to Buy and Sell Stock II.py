class Solution(object):
    def maxProfit(self, prices):
        profit = 0

        for i in range(1, len(prices)):
            profit += max(0, prices[i] - prices[i - 1])

        return profit

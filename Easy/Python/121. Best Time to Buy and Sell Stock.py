class Solution(object):
    def maxProfit(self, prices):
        buy = 0
        sell = 1
        maximum = 0

        # Use a sliding window to find the maximum
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maximum = max(maximum, profit)
            else:
                buy = sell
            sell += 1

        return maximum

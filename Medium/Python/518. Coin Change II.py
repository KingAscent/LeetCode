class Solution(object):
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins)):
            for j in range(coins[i], amount + 1, 1):
                dp[j] += dp[j - coins[i]]

        return dp[amount]

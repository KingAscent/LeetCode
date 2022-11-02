class Solution(object):
    def maximumWealth(self, accounts):
        # Keep track of the richest customer
        richest = 0
        
        # Go over the 2-dimensional int array adding up each customer's
        # money, and then compare their money to the richest customer
        for i in range(len(accounts)):
            wealth = 0
            for j in range(len(accounts[i])):
                wealth += accounts[i][j]
            if richest < wealth:
                richest = wealth
        
        # Return the richest customer's wealth
        return richest

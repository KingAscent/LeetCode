class Solution(object):
    def maxCoins(self, piles):
        # Sort the list, then initialize a variable to contain the maximum
        # number of coins that you can have, and initialize a variable of len(piles)
        piles.sort()
        maximum = 0
        length = len(piles)

        # Use a for loop to distribute the coins
        for i in range(length / 3, length - 1, 2):
            maximum += piles[i]

        # Return the maximum number of coins you can have
        return maximum

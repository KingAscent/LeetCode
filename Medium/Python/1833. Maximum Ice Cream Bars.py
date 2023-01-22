class Solution(object):
    def maxIceCream(self, costs, coins):
        # Counting Sort Algorithm
        # Find the max in the array
        maximum = costs[0]
        for c in costs:
            maximum = max(c, maximum)
        
        # Find the frequency of each cost
        costFreq = [0] * (maximum + 1)
        for c in costs:
            costFreq[c] += 1

        # Buy the lowest cost ice cream bars to maximize
        # amount of ice cream bars purchased
        count = 0
        for i in range(1, maximum + 1):
            freq = costFreq[i]
            if coins < i:
                break
            buy = min(freq, coins / i)
            coins -= i * buy
            count += buy
        
        return count

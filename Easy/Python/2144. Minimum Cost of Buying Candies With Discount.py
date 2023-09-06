class Solution(object):
    def minimumCost(self, cost):
        cost.sort()
        minCost = 0
        n = len(cost)

        for i in range(n):
            if i % 3 != n % 3:
                minCost += cost[i]
        
        return minCost

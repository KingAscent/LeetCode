class Solution(object):
    def minCostClimbingStairs(self, cost):
        first = cost[0]
        second = cost[1]

        for i in range(2, len(cost)):
            curr = cost[i] + min(first, second)
            first = second
            second = curr

        return min(first, second)

class Solution(object):
    def maxJump(self, stones):
        cost = stones[1]

        for i in range(2, len(stones)):
            cost = max(cost, stones[i] - stones[i - 2])
        
        return cost

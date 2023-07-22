class Solution(object):
    def lastStoneWeight(self, stones):
        stones.sort()
        n = len(stones)
        if n == 1:
            return stones[0]
        
        while 0 < stones[n - 2]:
            temp = stones[n - 1] - stones[n - 2]
            stones[n - 2] = 0
            stones[n - 1] = temp
            stones.sort()

        return stones[n - 1]

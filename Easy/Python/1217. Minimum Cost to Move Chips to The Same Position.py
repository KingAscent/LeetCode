class Solution(object):
    def minCostToMoveChips(self, position):
        even = 0
        odd = 0

        for pos in position:
            if pos % 2 == 0:
                even += 1
            else:
                odd += 1
        
        return min(even, odd)

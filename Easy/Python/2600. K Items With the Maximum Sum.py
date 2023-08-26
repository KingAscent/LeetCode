class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        return min(k, numOnes) - max(0, k - numOnes - numZeros)

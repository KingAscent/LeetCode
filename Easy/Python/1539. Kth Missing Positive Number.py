class Solution(object):
    def findKthPositive(self, arr, k):
        for n in arr:
            if n <= k:
                k += 1
            else:
                break
        
        return k

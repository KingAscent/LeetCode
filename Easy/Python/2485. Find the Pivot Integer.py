class Solution(object):
    def pivotInteger(self, n):
        pivot = -1
        left = 0

        for i in range(n + 1):
            left = left + i
            right = 0

            for j in range(i, n + 1):
                right = right + j
            
            if left == right:
                pivot = i
        
        return pivot

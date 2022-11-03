class Solution(object):
    def smallestEvenMultiple(self, n):
        min = n * 2
        if(n % 2 == 0):
            min = n
        return min

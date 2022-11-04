class Solution(object):
    def subtractProductAndSum(self, n):
        product = 1
        added = 0
        
        while 0 < n:
            product *= n % 10
            added += n % 10
            n = n / 10
        
        return product - added

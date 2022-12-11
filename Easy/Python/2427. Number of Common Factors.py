class Solution(object):
    def commonFactors(self, a, b):
        factors = 0
        maximum = max(a, b)

        for i in range(1, maximum + 1):
            if a % i == 0 and b % i == 0:
                factors += 1
        
        return factors

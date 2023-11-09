class Solution(object):
    def bitwiseComplement(self, n):
        complement = 1

        while complement < n:
            complement = complement * 2 + 1

        return complement - n
        

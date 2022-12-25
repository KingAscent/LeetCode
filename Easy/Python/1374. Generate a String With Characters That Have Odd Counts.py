class Solution(object):
    def generateTheString(self, n):
        odd = ''

        for i in range(n - 1):
            odd = odd + 'a'
        
        if n % 2 == 0:
            odd = odd + 'b'
        else:
            odd = odd + 'a'
        
        return odd

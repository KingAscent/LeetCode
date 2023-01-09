class Solution(object):
    def fib(self, n):
        if n <= 1:
            return n
        
        a = 0
        b = 1
        for i in range(1, n):
            temp = a
            a = b
            b = b + temp
        
        return b

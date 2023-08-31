class Solution(object):
    def minNumberOperations(self, target):
        ops = 0
        prev = 0

        for n in target:
            if prev < n:
                ops += n - prev
            prev = n
        
        return ops

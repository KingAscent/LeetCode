class Solution(object):
    def numberOfMatches(self, n):
        # Base case
        if n <= 2:
            return n / 2
        
        # Recursive cases
        if n % 2 == 0:
            return n / 2 + self.numberOfMatches(n / 2)
        else:
            return ((n - 1) / 2) + self.numberOfMatches((n - 1) / 2 + 1)

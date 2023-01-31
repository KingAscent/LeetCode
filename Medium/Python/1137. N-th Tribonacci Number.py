class Solution(object):
    def tribonacci(self, n):
        # Restrictions of n
        if n < 3:
            if n == 2:
                return 1
            return n
        
        # Initialize list to contain all the values of the Tribonacci sequence
        tri = [0] * (n + 1)
        tri[1] = 1
        tri[2] = 1

        # Calculate the nth value of the Tribonacci sequence by filling the list
        for i in range(3, n + 1):
            tri[i] = tri[i - 1] + tri[i - 2] + tri[i - 3]

        # Return the nth value of the Tribonacci sequence
        return tri[n]

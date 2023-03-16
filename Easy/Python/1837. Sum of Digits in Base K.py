class Solution(object):
    def sumBase(self, n, k):
        count = 0

        while n != 0:
            count += n % k
            n /= k

        return count

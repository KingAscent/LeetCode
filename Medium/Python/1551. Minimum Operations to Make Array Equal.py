class Solution(object):
    def minOperations(self, n):
        count = 0

        for i in range((2 * n - 2) / 2, -1, -2):
            count += i

        return count

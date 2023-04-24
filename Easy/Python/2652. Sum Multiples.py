class Solution(object):
    def sumOfMultiples(self, n):
        this_sum = 0

        for i in range(0, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                this_sum += i

        return this_sum

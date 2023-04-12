class Solution(object):
    def hammingDistance(self, x, y):
        num = 0

        while 0 < x or 0 < y:
            if x % 2 != y % 2:
                num += 1
            x /= 2
            y /= 2

        return num

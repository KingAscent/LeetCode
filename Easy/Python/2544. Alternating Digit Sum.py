class Solution(object):
    def alternateDigitSum(self, n):
        num = str(n)
        altSum = 0

        for i in range(len(num)):
            if i % 2 == 0:
                altSum += int(num[i])
            else:
                altSum -= int(num[i])

        return altSum

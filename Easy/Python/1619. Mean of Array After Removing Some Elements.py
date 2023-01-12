class Solution(object):
    def trimMean(self, arr):
        sum = 0
        fivePercent = len(arr) / 20
        arr.sort()

        for i in range(fivePercent, len(arr) - fivePercent):
            sum = sum + arr[i]

        return (sum * 1.0) / (len(arr) - (2 * fivePercent))

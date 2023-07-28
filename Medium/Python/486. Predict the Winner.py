class Solution(object):
    def PredictTheWinner(self, nums):
        n = len(nums)
        diff = [0] * n

        for i in range(n - 1, -1, -1):
            diff[i] = nums[i]
            for j in range(i + 1, n):
                diff[j] = max(nums[i] - diff[j], nums[j] - diff[j - 1])

        return 0 <= diff[n - 1]

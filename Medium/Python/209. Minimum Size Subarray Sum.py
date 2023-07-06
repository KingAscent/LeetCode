class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        minLen = n + 1
        j = 0
        this_sum = 0

        for i in range(n):
            this_sum += nums[i]
            while target <= this_sum:
                currLen = i - j + 1
                minLen = min(minLen, currLen)
                this_sum -= nums[j]
                j += 1

        if minLen != n + 1:
            return minLen
        else:
            return 0

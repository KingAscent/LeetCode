class Solution(object):
    def maximizeSum(self, nums, k):
        count = 0
        maximum = 0

        for i in range(len(nums)):
            maximum = max(maximum, nums[i])
        
        while 0 < k:
            count += maximum
            maximum += 1
            k -= 1

        return count

class Solution(object):
    def getMinDistance(self, nums, target, start):
        n = len(nums)

        for i in range(len(nums)):
            if nums[i] == target:
                n = min(n, abs(i - start))

        return n

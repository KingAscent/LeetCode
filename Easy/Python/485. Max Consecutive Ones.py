class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        track = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                track += 1
            else:
                track = 0
            count = max(count, track)

        return count

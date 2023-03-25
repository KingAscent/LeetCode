class Solution(object):
    def kLengthApart(self, nums, k):
        last = -1

        for i in range(len(nums)):
            if nums[i] == 1:
                if last != -1 and i - last <= k:
                    return False
                last = i

        return True

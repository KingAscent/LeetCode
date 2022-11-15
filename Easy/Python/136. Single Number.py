class Solution(object):
    def singleNumber(self, nums):
        single = 0
        for i in range(len(nums)):
            single = single ^ nums[i]
        return single

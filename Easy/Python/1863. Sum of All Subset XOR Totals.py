class Solution(object):
    def subsetXORSumHelper(self, nums, i, j):
        if i == len(nums):
            return j
        return self.subsetXORSumHelper(nums, i + 1, j^nums[i]) + self.subsetXORSumHelper(nums, i + 1, j)

    def subsetXORSum(self, nums):
        return self.subsetXORSumHelper(nums, 0, 0)

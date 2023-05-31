class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        two_negatives = nums[0] * nums[1] * nums[len(nums) - 1]
        no_negatives = nums[len(nums) - 1] * nums[len(nums) - 2] * nums[len(nums) - 3]
        return max(no_negatives, two_negatives)

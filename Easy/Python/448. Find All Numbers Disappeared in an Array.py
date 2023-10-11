class Solution(object):
    def findDisappearedNumbers(self, nums):
        missing = []
        count = [0] * len(nums)

        for i in range(len(nums)):
            count[nums[i] - 1] += 1
        for i in range(len(nums)):
            if count[i] == 0:
                missing.append(i + 1)
        
        return missing

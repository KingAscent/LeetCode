class Solution(object):
    def findFinalValue(self, nums, original):
        nums.sort()

        for i in range(len(nums)):
            if nums[i] == original:
                original *= 2
            elif original < nums[i]:
                break
        
        return original

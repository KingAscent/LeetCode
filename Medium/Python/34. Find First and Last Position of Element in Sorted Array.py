class Solution(object):
    def findFirst(self, nums, i, target):
        while i < len(nums):
            if nums[i] == target:
                return i
            else:
                i += 1

        # Target wasn't found, so return -1
        return -1
    

    def findLast(self, nums, j, target):
        while 0 <= j:
            if nums[j] == target:
                return j
            else:
                j -= 1

        # Target wasn't found, so return -1
        return -1


    def searchRange(self, nums, target):
        # Find the first appearance of the target
        first = self.findFirst(nums, 0, target)

        # Find the last appearance of the target and return a list
        # containing the first and last appearance indeces
        return [first, self.findLast(nums, len(nums) - 1, target)]

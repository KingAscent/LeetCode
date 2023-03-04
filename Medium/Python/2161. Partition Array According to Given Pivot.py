class Solution(object):
    def pivotArray(self, nums, pivot):
        length = len(nums)
        rearranged = [0] * length
        index = 0

        for i in range(length):
            if nums[i] < pivot:
                rearranged[index] = nums[i]
                index += 1
        
        for i in range(length):
            if nums[i] == pivot:
                rearranged[index] = nums[i]
                index += 1
        
        for i in range(length):
            if pivot < nums[i]:
                rearranged[index] = nums[i]
                index += 1
        
        return rearranged

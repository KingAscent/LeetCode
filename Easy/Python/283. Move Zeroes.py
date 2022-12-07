class Solution(object):
    def moveZeroes(self, nums):
        end = len(nums)
        i = 0
        while i < end:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                end -= 1
            else:
                i += 1

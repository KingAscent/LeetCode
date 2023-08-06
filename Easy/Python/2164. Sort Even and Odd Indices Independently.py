class Solution(object):
    def sortEvenOdd(self, nums):
        # Evens
        for i in range(0, len(nums), 2):
            for j in range(i + 2, len(nums), 2):
                if nums[j] <= nums[i]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        
        # Odds
        for i in range(1, len(nums), 2):
            for j in range(i + 2, len(nums), 2):
                if nums[i] <= nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp

        return nums

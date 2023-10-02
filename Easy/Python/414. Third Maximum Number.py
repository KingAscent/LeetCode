class Solution(object):
    def thirdMax(self, nums):
        nums.sort()
        count = 0
        third = nums[0]

        for i in range(len(nums) - 1, -1, -1):
            if third != nums[i]:
                third = nums[i]
                count += 1
            if count == 3:
                break
        
        return third if count == 3 else nums[len(nums) - 1]

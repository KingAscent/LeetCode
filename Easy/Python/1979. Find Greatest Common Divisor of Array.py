class Solution(object):
    def findGCD(self, nums):
        nums.sort()
        minimum = nums[0]
        maximum = nums[len(nums) - 1]
        greatest = 0

        for i in range(1, maximum + 1):
            if maximum % i == 0 and minimum % i == 0:
                greatest = i

        return greatest

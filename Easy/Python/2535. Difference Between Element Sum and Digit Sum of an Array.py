class Solution(object):
    def differenceOfSum(self, nums):
        digitSum = 0
        listSum = 0

        for i in range(len(nums)):
            listSum += nums[i]
            while nums[i] != 0:
                digitSum += nums[i] % 10
                nums[i] /= 10

        return abs(digitSum - listSum)

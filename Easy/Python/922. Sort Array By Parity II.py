class Solution(object):
    def sortArrayByParityII(self, nums):
        parity = [0] * len(nums)
        even = 0
        odd = 1

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                parity[even] = nums[i]
                even += 2
            else:
                parity[odd] = nums[i]
                odd += 2

        return parity

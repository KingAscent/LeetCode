class Solution(object):
    def findNumbers(self, nums):
        count = 0

        for i in nums:
            digits = 0
            while(0 < i):
                digits += 1
                i = i / 10
            if digits % 2 == 0:
                count += 1

        return count

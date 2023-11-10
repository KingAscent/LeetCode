class Solution(object):
    def averageValue(self, nums):
        count = 0
        avg = 0

        for n in nums:
            if n % 6 == 0:
                avg += n
                count += 1
        
        return 0 if avg == 0 else avg / count

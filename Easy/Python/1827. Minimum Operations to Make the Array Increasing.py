class Solution(object):
    def minOperations(self, nums):
        count = 0
        prev = 0
        
        for n in nums:
            if n <= prev:
                count += prev + 1 - n
                prev += 1
            else:
                prev = n

        return count

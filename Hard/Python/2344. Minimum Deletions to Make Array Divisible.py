class Solution(object):
    def minOperations(self, nums, numsDivide):
        # Initialize a greatest common divisor and a temp value
        gcd = numsDivide[0]
        temp = 0

        # Find the greatest common divisor of numsDivide
        for i in numsDivide:
            while 0 < i:
                temp = gcd % i
                gcd = i
                i = temp
        
        # Sort the nums list, then ignore any elements in nums that
        # are smaller than gcd. Return the smallest element nums[i]
        # that divides gcd
        nums.sort()
        for i, j in enumerate(nums):
            if gcd % j == 0:
                return i
        
        # No such element exists in nums, return -1
        return -1

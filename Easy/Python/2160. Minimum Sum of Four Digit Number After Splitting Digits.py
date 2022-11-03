class Solution(object):
    def minimumSum(self, num):
        # Get all 4 digits isolated into different elements of the list
        digits = [0, 1, 2, 3]
        for i in range(4):
            digits[i] = num % 10
            num = num / 10
        
        # Sort the list
        digits.sort()
        
        # Assuming the digits are labeled in ascending order, A -> D,
        # the minimum possible of sum of new1 + new2 is AD + BC
        new1 = (digits[0] * 10) + digits[3]
        new2 = (digits[1] * 10) + digits[2]
        return new1 + new2

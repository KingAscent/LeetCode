class Solution(object):
    def isHappy(self, n):
        while n != 1 and n != 4:
            this_sum = n
            n = 0
            while this_sum != 0:
                temp = this_sum % 10
                n += temp * temp
                this_sum = this_sum / 10
        
        return n == 1

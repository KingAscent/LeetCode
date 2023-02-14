class Solution(object):
    def countDigits(self, num):
        count = 0
        temp = num

        while temp != 0:
            if temp % 10 != 0 and num % (temp % 10) == 0:
                count += 1
            temp /= 10

        return count

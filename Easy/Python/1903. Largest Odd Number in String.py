class Solution(object):
    def largestOddNumber(self, num):
        i = len(num) - 1

        while 0 <= i:
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
            i -= 1
        
        return ''

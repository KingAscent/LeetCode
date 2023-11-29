class Solution(object):
    def convertToBase7(self, num):
        if num == 0:
            return '0'
            
        neg = '' if 0 <= num else '-'
        base7 = ''
        num = abs(num)

        while 1 <= num:
            base7 = str(num % 7) + base7
            num = num // 7
        
        return neg + base7

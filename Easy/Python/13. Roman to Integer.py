class Solution(object):
    def romanToInt(self, s):
        num = 0
        ans = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == 'I':
                num = 1
            elif s[i] == 'V':
                num = 5
            elif s[i] == 'X':
                num = 10
            elif s[i] == 'L':
                num = 50
            elif s[i] == 'C':
                num = 100
            elif s[i] == 'D':
                num = 500
            elif s[i] == 'M':
                num = 1000
            
            if num * 4 < ans:
                ans -= num
            else:
                ans += num

        return ans

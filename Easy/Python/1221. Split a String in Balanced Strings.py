class Solution(object):
    def balancedStringSplit(self, s):
        countR = 0
        countL = 0
        count = 0

        for i in range(len(s)):
            if s[i] == 'L':
                countL += 1
            else:
                countR += 1
            if countR == countL and countR != 0:
                count += 1
                countL = 0
                countR = 0

        return count

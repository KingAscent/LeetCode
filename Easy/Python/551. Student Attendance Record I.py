class Solution(object):
    def checkRecord(self, s):
        countAbsent = 0

        for i in range(len(s)):
            if(s[i] == 'A'):
                countAbsent += 1
            if(i < len(s) - 2) and (s[i:i + 3] == "LLL"):
                return False
        
        return countAbsent < 2

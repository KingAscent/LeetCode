class Solution(object):
    def checkString(self, s):
        found = False

        for i in range(len(s)):
            if s[i] == 'b':
                found = True
            if found and s[i] == 'a':
                return False

        return True

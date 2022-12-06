class Solution(object):
    def firstUniqChar(self, s):
        myDict = {}

        for c in s:
            if c not in myDict:
                myDict[c] = 1
            else:
                myDict[c] = myDict.get(c) + 1
        
        for i in range(len(s)):
            if myDict[s[i]] == 1:
                return i
        
        return -1

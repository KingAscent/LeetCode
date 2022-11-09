class Solution(object):
    def countAsterisks(self, s):
        count = 0
        isBarred = False

        # Look through the string, when a bar is found
        # ignore any asterisks found
        for i in range(len(s)):
            if(not isBarred and s[i] == '|'):
                isBarred = True
            elif(isBarred and s[i] == '|'):
                isBarred = False
            if(not isBarred and s[i] == '*'):
                count += 1
        
        return count

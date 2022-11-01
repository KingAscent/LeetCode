class Solution(object):
    def lengthOfLastWord(self, s):
        # Boolean value to keep track of when a word is found
        # Length of the longest last word
        wordFound = False
        length = 0
        
        # Go over the string looking for the last word
        for i in reversed(range(len(s))):
            if(s[i] != ' '):
                wordFound = True
                length += 1
            if(wordFound and s[i] == ' '):
                return length
        
        return length

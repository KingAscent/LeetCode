class Solution(object):
    def isAcronym(self, words, s):
        sb = ""

        for word in words:
            sb += word[0]
        
        return sb == s
        

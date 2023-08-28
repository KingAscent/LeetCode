class Solution(object):
    def repeatedSubstringPattern(self, s):
        # Append the string twice, then drop the first and last letter.
        # See if the result still has the original string s.
        dropped = (s + s)[1:(len(s) * 2) - 1]
        return s in dropped

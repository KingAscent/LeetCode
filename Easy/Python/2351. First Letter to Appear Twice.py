class Solution(object):
    def repeatedCharacter(self, s):
        count = {}
        twice = 'a'

        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = 1
            else:
                twice = s[i]
                break
        
        return twice

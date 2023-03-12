class Solution(object):
    def removeStars(self, s):
        starless = []

        for c in s:
            if c != '*':
                starless += c
            else:
                starless.pop()

        return ''.join(starless)

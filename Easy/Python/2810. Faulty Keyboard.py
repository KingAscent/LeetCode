class Solution(object):
    def finalString(self, s):
        sb = ""

        for c in s:
            if c == 'i':
                sb = sb[::-1]
            else:
                sb += c
        
        return sb

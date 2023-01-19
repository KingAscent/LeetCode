class Solution(object):
    def percentageLetter(self, s, letter):
        count = 0

        for c in s:
            if c == letter:
                count += 1
        
        return int((float(count) / float(len(s))) * 100)

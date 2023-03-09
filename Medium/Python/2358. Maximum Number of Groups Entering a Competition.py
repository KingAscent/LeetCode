class Solution(object):
    def maximumGroups(self, grades):
        maximum = 0
        total = 0

        while maximum + total + 1 <= len(grades):
            maximum += 1
            total += maximum
        
        return maximum

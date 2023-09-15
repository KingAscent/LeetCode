class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        countL = 0
        countR = 0
        countBlanks = 0

        for i in range(len(moves)):
            if moves[i] == 'L':
                countL += 1
            elif moves[i] == 'R':
                countR += 1
            else:
                countBlanks += 1
        
        return abs(countL - countR) + countBlanks

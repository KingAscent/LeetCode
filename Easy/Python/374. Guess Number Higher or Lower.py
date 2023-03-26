class Solution(object):
    def guessNumber(self, n):
        if n == 1:
            return 1
        if guess(n) == 0:
            return n
        
        first = 1
        last = n
        pick = 0

        while first < last:
            pick = first + (last - first) / 2
            temp = guess(pick)
            if temp == 0:
                break
            elif temp == -1:
                last = pick
            else:
                first = pick

        return pick

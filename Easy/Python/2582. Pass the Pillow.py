class Solution(object):
    def passThePillow(self, n, time):
        place = 0
        direction = time / (n - 1)
        remainder = time % (n - 1)

        if direction % 2 == 0:
            place = remainder + 1
        else:
            place = n - remainder
        
        return place

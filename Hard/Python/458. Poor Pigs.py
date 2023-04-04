class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        pigs = 0

        while pow(minutesToTest / minutesToDie + 1, pigs) < buckets:
            pigs += 1

        return pigs

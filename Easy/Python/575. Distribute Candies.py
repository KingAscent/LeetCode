class Solution(object):
    def distributeCandies(self, candyType):
        limit = len(candyType) / 2
        this_set = set(candyType)

        if len(this_set) <= limit:
            return len(this_set)
        else:
            return limit

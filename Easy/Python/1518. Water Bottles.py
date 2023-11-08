class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        count = numBottles

        while numExchange <= numBottles:
            temp = numBottles / numExchange
            count += temp
            numBottles = temp + (numBottles - (numExchange * temp))

        return count

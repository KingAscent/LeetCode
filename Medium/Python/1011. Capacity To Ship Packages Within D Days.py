class Solution(object):
    def shipWithinDays(self, weights, days):
        start = 0
        end = 0

        for i in weights:
            start = max(start, i)
            end += i
        
        while start <= end:
            mid = start + ((end - start) / 2)
            cap = self.findDay(weights, mid)
            if cap <= days:
                end = mid - 1
            else:
                start = mid + 1
        
        return start
    
    def findDay(self, weights, mid):
        date = 0
        tempSum = 0

        for i in range(len(weights)):
            if tempSum + weights[i] <= mid:
                tempSum += weights[i]
            else:
                tempSum = weights[i]
                date += 1
        
        return date + 1

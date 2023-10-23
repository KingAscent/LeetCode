class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        sec = duration
        
        for i in range(1, len(timeSeries)):
            sec += min(duration, timeSeries[i] - timeSeries[i - 1])
        
        return sec

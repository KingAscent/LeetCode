class Solution(object):
    def maxSatisfaction(self, satisfaction):
        satisfaction.sort()
        n = len(satisfaction)
        sums = [0] * (n + 1)
        score = 0
        maxScore = 0

        # Use a for loop to calculate the sum from right to left
        for i in range(n - 1, -1, -1):
            sums[i] = sums[i + 1] + satisfaction[i]
            score += (i + 1) * satisfaction[i]
        
        if 0 < score:
            maxScore = score
        
        for i in range(n):
            score -= satisfaction[i]
            score -= sums[i + 1]
            if maxScore < score:
                maxScore = score
        
        return maxScore

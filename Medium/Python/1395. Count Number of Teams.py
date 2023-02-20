class Solution(object):
    def numTeams(self, rating):
        count = 0

        for i in range(len(rating)):
            left = 0
            right = 0
            for j in range(0, i):
                if rating[j] < rating[i]:
                    left += 1
            for k in range(i + 1, len(rating)):
                if rating[i] < rating[k]:
                    right += 1
            count += (left * right) + (i - left) * (len(rating) - i - right - 1)

        return count

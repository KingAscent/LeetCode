class Solution(object):
    def captureForts(self, forts):
        this_sum = 0
        count = 0
        this_max = 0

        for i in range(len(forts)):
            if forts[i] != 0:
                this_sum += forts[i]
                if this_sum == 0:
                    this_max = max(this_max, count)
                this_sum = forts[i]
                count = 0
            elif this_sum != 0:
                count += 1
        
        return this_max

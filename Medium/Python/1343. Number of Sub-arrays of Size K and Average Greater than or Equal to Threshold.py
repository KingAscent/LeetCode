class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        count = 0
        this_sum = 0
        this_avg = 0

        for i in range(len(arr)):
            this_sum += arr[i]
            if k - 1 <= i:
                this_avg = this_sum / k
                if threshold <= this_avg:
                    count += 1
                this_sum -= arr[i - (k - 1)]

        return count

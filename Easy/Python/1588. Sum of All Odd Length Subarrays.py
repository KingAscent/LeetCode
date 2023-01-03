class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        sum = 0

        # Count each element in an odd-length sub-array and multiply
        # the array elements to get the output of the sum
        for i in range(len(arr)):
            present = ((i + 1) * (len(arr) - i) + 1) / 2
            sum = sum + (present * arr[i])

        return sum

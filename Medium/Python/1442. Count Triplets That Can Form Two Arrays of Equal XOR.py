class Solution(object):
    def countTriplets(self, arr):
        count = 0

        for i in range(len(arr)):
            temp = arr[i]
            for j in range(i + 1, len(arr)):
                # xor of element
                temp ^= arr[j]
                if temp == 0:
                    count += j - i

        return count

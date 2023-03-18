class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        count = 0

        for i in range(len(arr1)):
            dist = 0
            for j in range(len(arr2)):
                diff = abs(arr1[i] - arr2[j])
                if diff <= d:
                    j = len(arr2)
                else:
                    dist += 1
            if dist == len(arr2):
                count += 1

        return count

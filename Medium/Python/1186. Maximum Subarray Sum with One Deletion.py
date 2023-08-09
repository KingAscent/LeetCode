class Solution(object):
    def maximumSum(self, arr):
        n = len(arr)
        front = [0] * n
        back = [0] * n
        maxSum = arr[0]

        # Going forward
        front[0] = arr[0]
        for i in range(1, n, 1):
            front[i] = max(arr[i], front[i - 1] + arr[i])
            maxSum = max(maxSum, front[i])
        
        # Going back
        back[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            back[i] = max(arr[i], back[i + 1] + arr[i])
        
        # Find max sum
        for i in range(1, n - 1, 1):
            maxSum = max(maxSum, front[i - 1] + back[i + 1])

        return maxSum

class Solution(object):
    def rotate(self, nums, k):
        # In the event k is larger than len(nums),
        # simplify so to not rotate in circles
        n = len(nums)
        k %= n
        temp = [0] * n

        for i in range(n):
            temp[(i + k) % n] = nums[i]
        
        for i in range(n):
            nums[i] = temp[i]

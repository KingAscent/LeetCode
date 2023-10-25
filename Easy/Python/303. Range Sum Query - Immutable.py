class NumArray(object):
    def __init__(self, nums):
        self.arr = nums
        

    def sumRange(self, left, right):
        this_sum = 0

        for i in range(left, right + 1):
            this_sum += self.arr[i]
        
        return this_sum

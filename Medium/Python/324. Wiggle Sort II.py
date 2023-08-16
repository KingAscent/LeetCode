class Solution(object):
    def wiggleSort(self, nums):
        nums.sort()
        mid = (len(nums) - 1) / 2
        end = len(nums) - 1
        store = [0] * (end + 1)
        count = 0

        while 0 <= mid or (len(nums) - 1) / 2 < end:
            if count % 2 == 0:
                store[count] = nums[mid]
                mid -= 1
            else:
                store[count] = nums[end]
                end -= 1
            count += 1
        
        for i in range(len(nums)):
            nums[i] = store[i]

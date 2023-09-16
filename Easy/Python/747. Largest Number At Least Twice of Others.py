class Solution(object):
    def dominantIndex(self, nums):
        largest = 0        # Index of largest element
        secondLargest = 1  # Index of second largest element

        for i in range(1, len(nums)):
            if nums[largest] < nums[i]:
                secondLargest = largest
                largest = i
            elif nums[secondLargest] < nums[i]:
                secondLargest = i
        
        return largest if nums[secondLargest] * 2 <= nums[largest] else -1

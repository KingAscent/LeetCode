class Solution(object):
    def decompressRLElist(self, nums):
        # Initialize a list that will contain all values
        decompressedList = []

        # Add all the values into the decompressed list a
        # frequency number of times
        for i in range(0, len(nums), 2):
            freq = nums[i]
            value = nums[i + 1]
            for j in range(freq):
                decompressedList.append(value)
        
        # Return the decompressedList
        return decompressedList

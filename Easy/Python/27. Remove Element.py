class Solution(object):
    def removeElement(self, nums, val):
        # Intialize a count to keep track of elements
        count = 0
        
        # Go over the array, shifting leftward if a value
        # is found and is the same as val
        for i in range(len(nums)):
            if(nums[i] != val):
                nums[count] = nums[i]
                count += 1
        
        # Return the count of elements left in the array
        return count

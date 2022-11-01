class Solution(object):
    def removeDuplicates(self, nums):
        # Index 0 will never be a duplicate of a number before it
        count = 1
        
        # Go over the array shifting the array leftward if it
        # encounters ad uplicatre number
        for i in range(1, len(nums)):
            if(nums[i - 1] != nums[i]):
                nums[count] = nums[i]
                count += 1
        
        # Return the count of distinct numbers in the array
        return count

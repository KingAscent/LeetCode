class Solution(object):
    def smallestDistancePair(self, nums, k):
        # Sort the list, then initialize a minimum and maximum variable
        nums.sort()
        minimum = 0
        maximum = nums[len(nums) - 1] - nums[0]

        # Binary search algorithm
        while minimum < maximum:
            mid = (minimum + maximum) / 2
            count = 0
            i = 0

            # Find pairs with distance less than or equal to middle
            for j in range(len(nums)):
                # Run through this segment of code once, then break
                while True:
                    diff = nums[j] - nums[i]
                    if mid < diff:
                        i += 1
                    else:
                        break
                count += j - i
        
            if k <= count:
                maximum = mid
            else:
                minimum = mid + 1
        
        # Return the smallest distance found
        return minimum

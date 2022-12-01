class Solution(object):
    def minPairSum(self, nums):
        # Sort the list, initialize an index for a new list, initialize new list
        nums.sort()
        index = 0
        pairs = [0] * (len(nums) / 2)

        # Use a for loop to travel over nums, placing each pair
        # Increase the index value after each pair is added
        for i in range(len(nums) / 2):
            pairs[index] = nums[i] + nums[len(nums) - i - 1]
            index += 1

        # Initialize a max value equal to the first integer in pairs
        # For each integer in pairs, compare it to max and set max to the larger
        maximum = 0
        for i in pairs:
            maximum = max(i, maximum)

        # Return maximum
        return maximum

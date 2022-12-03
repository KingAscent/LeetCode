class Solution(object):
    def countDistinctIntegers(self, nums):
        # Initialize a set to keep track of each individual num
        # Sets do not allow duplicate elements so similar numbers are ignored
        numbers = set()

        # For each number in nums, first add the number
        # Then reverse the number and add it to the set
        for n in nums:
            numbers.add(n)
            numR = 0 # Variable for the number reversed
            while n != 0:
                # Evaluate each number in reverse order
                numR = numR * 10 + (n % 10)
                n = n / 10
            numbers.add(numR)

        # Return the size of the set
        return len(numbers)

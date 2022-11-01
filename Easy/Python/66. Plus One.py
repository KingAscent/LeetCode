class Solution(object):
    def plusOne(self, digits):
        # Go over the array, checking to see if the end of it is
        # a string of 9's (Example: 9, 9, 9, 9)
        for i in reversed(range(len(digits))):
            # If the end is not a string of 9's, raise the digit
            # and exit the loop
            if(digits[i] != 9):
                digits[i] += 1
                break
            else:
                # A 9 is found, change the digits to a 0
                digits[i] = 0
        
        # If the entire array was a string of 9's, create a new
        # array with a leading 1. Then return the array
        if(digits[0] == 0):
            nums = [len(digits)]
            nums[0] = 1
            for i in range(len(digits)):
                nums.append(0)
            return nums
        
        # Return digits after incrementing the last element
        return digits

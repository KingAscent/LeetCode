class Solution(object):
    def convert(self, s, numRows):
        # Filter out strings on a singular row
        if numRows == 1:
            return s
        
        # Initialize a variable to contain the new string, the string length,
        # and a variable that has the step for each character's indentation
        zigZag = ""
        length = len(s)
        step = 2 * (numRows - 1)

        # Use a for loop to design each row
        for i in range(numRows):
            # Use a for loop to place each character in the row
            for j in range(i, length, step):
                zigZag += s[j]
                if i != 0 and i != (step / 2) and (j + step - 2 * i) < length:
                    zigZag += s[j + step - 2 * i]
        
        # Return the zigzag string
        return zigZag

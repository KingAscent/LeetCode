class Solution(object):
    def isPalindrome(self, x):
        # Convert x to a string, then find its length
        string = str(x)
        length = len(string)
        
        # Use a for loop to go over half of the string,
        # making sure that it is the same on both the
        # front and end of the string
        for i in range(length / 2):
            if(string[i] != string[length - i - 1]):
                return False
        return True

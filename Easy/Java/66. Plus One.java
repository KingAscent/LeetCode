class Solution {
    public int[] plusOne(int[] digits) {
        // Go over the array, checking to see if the end of it is
        // a string of 9's (Example: 9, 9, 9, 9)
        for(int i = digits.length - 1; 0 <= i; i--){
            // If the end is not a string of 9's, raise the digit
            // and exit the loop
            if(digits[i] != 9){
                digits[i]++;
                i = -1;
            }else{
                // A 9 is found, change the digit to a 0
                digits[i] = 0;
            }
        }
        
        // If the entire array was a string of 9's, create a new
        // array with a leading 1. Then return the array
        if(digits[0] == 0){
            int[] nums = new int[digits.length + 1];
            nums[0] = 1;
            return nums;
        }
        
        // Return digits after incrementing the last element
        return digits;
    }
}

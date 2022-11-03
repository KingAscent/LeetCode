class Solution {
    public int minimumSum(int num) {
        // Get all 4 digits isolated into different elements of the array
        int[] digits = new int[4];
        for(int i = 0; i < 4; i++){
            digits[i] = num % 10;
            num = num / 10;
        }
        
        // Sort the array
        Arrays.sort(digits);
        
        // Assuming the digits are labeled in ascending order, A -> D,
        // the minimum possible of sum of new1 + new2 is AD + BC
        int new1 = (digits[0] * 10) + digits[3];
        int new2 = (digits[1] * 10) + digits[2];
        return new1 + new2;
    }
}

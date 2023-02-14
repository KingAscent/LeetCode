class Solution {
    public int maxSubArray(int[] nums) {
        // Initialize 2 variables to keep track of the sum
        int sum = nums[0];
        int tempSum = sum;

        // Use a for loop to see what the largest subarray is
        for(int i = 1; i < nums.length; i++){
            tempSum = Math.max(tempSum + nums[i], nums[i]);
            sum = Math.max(tempSum, sum);
        }
        
        // Return the largest subarray sum
        return sum;
    }
}

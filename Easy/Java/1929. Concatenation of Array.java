class Solution {
    public int[] getConcatenation(int[] nums) {
        // Create a new integer array to contain all the values
        int[] nums2 = new int[nums.length * 2];

        // Go over the array adding the values into both spots
        // that they appear in the new array
        for(int i = 0; i < nums.length; i++){
            nums2[i] = nums2[i + nums.length] = nums[i];
        }

        // Return the new integer array
        return nums2;
    }
}

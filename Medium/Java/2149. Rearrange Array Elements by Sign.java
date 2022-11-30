class Solution {
    public int[] rearrangeArray(int[] nums) {
        // Create a new array, an even index, and odd index variable
        int[] rearranged = new int[nums.length];
        int i = 0; // Even index
        int j = 1; // Odd index

        // Go over the array adding positives, then negatives, to the array
        for(int k = 0; k < nums.length; k++){
            if(0 < nums[k]){
                rearranged[i] = nums[k];
                i += 2;
            }else{
                rearranged[j] = nums[k];
                j += 2;
            }
        }

        // Return the new array
        return rearranged;
    }
}

class Solution {
    public int triangularSum(int[] nums) {
        // Initialize a variable to contain number of elements 
        int tSum = nums.length;
        
        while(tSum != 1){
            // Run until every number has been added into the 0th index
            for(int i = 0; i < tSum - 1; i++)
                nums[i] = (nums[i] + nums[i + 1]) % 10;
            tSum--;
        }

        // Return the 0th index
        return nums[0];
    }
}

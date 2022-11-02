class Solution {
    public int numIdenticalPairs(int[] nums) {
        // Keep track of number of good pairs
        int count = 0;
        
        // Go over the array using a nested for loop, comparing
        // each element looking for good pairs
        for(int i = 0; i < nums.length - 1; i++){
            for(int j = 1; j < nums.length; j++){
                if(i < j && nums[i] == nums[j])
                    count++;
            }
        }
        
        // Return the number of good pairs
        return count;
    }
}

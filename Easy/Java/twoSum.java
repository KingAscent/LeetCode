class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Array to be returned
        int[] indeces = new int[2];
        
        // Go over the array of numbers, seeing if elements add
        // up to our target while not having the same indeces
        for(int i = 0; i < nums.length; i++){
            for(int j = i; j < nums.length; j++){
                if(i != j && nums[i] + nums[j] == target){
                    indeces[0] = i;
                    indeces[1] = j;
                }
            }
        }
        
        // Return the array
        return indeces;
    }
}

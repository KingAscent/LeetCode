class Solution {
    public int[] twoSum(int[] nums, int target) {
        // The array that will be returned
        int[] solution = new int[2];
        
        // Check each index's integer and see if they
        // add up to the target integer, and if so,
        // add their indexes to the solution array
        for(int i = 0; i < nums.length; i++){
            for(int j = i + 1; j < nums.length; j++){
                if(nums[i] + nums[j] == target){
                    solution[0] = i;
                    solution[1] = j;
                }
            }
        }
        return solution;
    }
}

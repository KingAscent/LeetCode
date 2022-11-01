class Solution {
    public int removeDuplicates(int[] nums) {
        // Index 0 will never be a duplicate of a number before it
        int count = 1;
        
        // Go over the array shifting the array leftward if it
        // encounters a duplicate number
        for(int i = 1; i < nums.length; i++){
            if(nums[i - 1] != nums[i]){
                nums[count] = nums[i];
                count++;
            }
        }
        
        // Return the count of distinct numbers in the array
        return count;
    }
}

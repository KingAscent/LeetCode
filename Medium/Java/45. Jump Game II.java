class Solution {
    public int jump(int[] nums) {
        // Initial values
        int max = 0;
        int jump = 0;
        int count = 0;
        
        // Use a for loop to check how far we can jump
        for(int i = 0; i < nums.length - 1; i++){
            max = Math.max(max, i + nums[i]);
            if(jump == i){
                jump = max;
                count++;
            }
        }

        // Return the number of jumps taken
        return count;
    }
}

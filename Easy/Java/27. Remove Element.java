class Solution {
    public int removeElement(int[] nums, int val) {
        // Initialize a count to keep track of elements
        int count = 0;
        
        // Go over the array, shifting leftward if a value
        // is found and is the same as val
        for(int i = 0; i < nums.length; i++){
            if(nums[i] != val){
                nums[count] = nums[i];
                count++;
            }
        }
        
        // Return the count of elements left in the array
        return count;
    }
}

class Solution {
    public int searchInsert(int[] nums, int target) {
        // Go over the array looking for the target, or when the
        // element is larger than the target number
        for(int i = 0; i < nums.length; i++){
            if(nums[i] == target || target < nums[i])
                return i;
        }
        
        // The target was not found and is larger than all
        // elements in the array
        return nums.length;
    }
}

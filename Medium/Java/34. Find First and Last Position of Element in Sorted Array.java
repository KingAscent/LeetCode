class Solution {
    public int[] searchRange(int[] nums, int target) {
        // Find the first appearance of the target
        int first = findFirst(nums, 0, target);

        // Find the last appearance of the target, and return an array
        // containing the first and last appearance indeces
        return new int[] {first, findLast(nums, nums.length - 1, target)};
    }

    public int findFirst(int[] nums, int i, int target){
        while(i < nums.length){
            if(nums[i] == target)
                return i;
            else
                i++;
        }
        
        // Target wasn't found, so return -1
        return -1;
    }

    public int findLast(int[] nums, int j, int target){
        while(0 <= j){
            if(nums[j] == target)
                return j;
            else
                j--;
        }

        // Target wasn't found, so return -1
        return -1;
    }
}

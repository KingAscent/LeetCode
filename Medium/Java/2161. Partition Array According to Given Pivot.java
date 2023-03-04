class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        int len = nums.length;
        int[] rearranged = new int[len];
        int index = 0;

        for(int i = 0; i < len; i++){
            if(nums[i] < pivot){
                rearranged[index] = nums[i];
                index++;
            }
        }

        for(int i = 0; i < len; i++){
            if(nums[i] == pivot){
                rearranged[index] = nums[i];
                index++;
            }
        }

        for(int i = 0; i < len; i++){
            if(pivot < nums[i]){
                rearranged[index] = nums[i];
                index++;
            }
        }

        return rearranged;
    }
}

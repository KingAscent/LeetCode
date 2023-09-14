class Solution {
    public int findMaxK(int[] nums) {
        Arrays.sort(nums);
        int start = 0;
        int end = nums.length - 1;
        int max = -1;
        if(0 < nums[start])
            return max;
        
        while(start < end){
            if(nums[start] + nums[end] == 0){
                max = nums[end];
                break;
            }else if(Math.abs(nums[start]) < nums[end]){
                end--;
            }else{
                start++;
            }
        }

        return max;
    }
}

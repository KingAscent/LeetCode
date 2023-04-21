class Solution {
    public int[] leftRigthDifference(int[] nums) {
        int left = 0;
        int right = 0;
        
        for(int n : nums){
            right += n;
        }

        for(int i = 0; i < nums.length; i++){
            left += nums[i];
            right -= nums[i];
            nums[i] = Math.abs((left - nums[i]) - right);
        }

        return nums;
    }
}

class Solution {
    public int maxAscendingSum(int[] nums) {
        int sum = nums[0];
        int maxSum = sum;

        for(int i = 1; i < nums.length; i++){
            if(nums[i - 1] < nums[i]){
                sum += nums[i];
            }else{
                maxSum = Math.max(maxSum, sum);
                sum = nums[i];
            }
            
        }

        return maxSum < sum ? sum : maxSum;
    }
}

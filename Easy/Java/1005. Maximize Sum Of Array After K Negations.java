class Solution {
    public int largestSumAfterKNegations(int[] nums, int k) {
        Arrays.sort(nums);
        int n = nums.length;

        for(int i = 0; i < n; i++){
            if(k != 0 && nums[i] < 0){
                nums[i] *= -1;
                k--;
            }else{
                break;
            }
        }

        if(k != 0){
            Arrays.sort(nums);
            while(k != 0){
                nums[0] *= -1;
                k--;
            }
        }

        int sum = 0;
        for(int i = 0; i < n; i++){
            sum += nums[i];
        }

        return sum;
    }
}

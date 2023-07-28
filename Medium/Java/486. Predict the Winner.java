class Solution {
    public boolean PredictTheWinner(int[] nums) {
        int n = nums.length;
        int[] diff = new int[n];

        for(int i = n - 1; 0 <= i; i--){
            diff[i] = nums[i];
            for(int j = i + 1; j < n; j++){
                diff[j] = Math.max(nums[i] - diff[j], nums[j] - diff[j - 1]);
            }
        }

        return 0 <= diff[n - 1];
    }
}

class Solution {
    public int minStartValue(int[] nums) {
        int sum = 0;

        for(int i = 0; i < nums.length; i++){
            sum += nums[i];
            nums[i] = sum;
        }

        Arrays.sort(nums);
        
        if(0 < nums[0])
            return 1;
        else
            return Math.abs(nums[0]) + 1;
    }
}

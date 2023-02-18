class Solution {
    public int differenceOfSum(int[] nums) {
        int digitSum = 0;
        int arraySum = 0;

        for(int i = 0; i < nums.length; i++){
            arraySum += nums[i];
            while(nums[i] != 0){
                digitSum += nums[i] % 10;
                nums[i] /= 10;
            }
        }

        return Math.abs(digitSum - arraySum);
    }
}

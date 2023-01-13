class Solution {
    public int findGCD(int[] nums) {
        Arrays.sort(nums);
        int min = nums[0];
        int max = nums[nums.length - 1];
        int greatest = 0;

        for(int i = 1; i <= max; i++){
            if(max % i == 0 && min % i == 0)
                greatest = i;
        }

        return greatest;
    }
}

class Solution {
    public int combinationSum4(int[] nums, int target) {
        int[] cases = new int[target + 1];
        cases[0] = 1;

        for(int i = 1; i <= target; i++){
            for(int n : nums){
                if(n <= i)
                    cases[i] += cases[i - n];
            }
        }

        return cases[target];
    }
}

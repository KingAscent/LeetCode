class Solution {
    public int maximizeSum(int[] nums, int k) {
        int count = 0;
        int max = 0;

        for(int i = 0; i < nums.length; i++){
            max = Math.max(max, nums[i]);
        }
        
        while(0 < k){
            count += max;
            max++;
            k--;
        }

        return count;
    }
}

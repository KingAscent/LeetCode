class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        int minLen = n + 1;
        int j = 0;
        int sum = 0;
        
        for(int i = 0; i < n; i++){
            sum += nums[i];
            while(target <= sum){
                int currLen = i - j + 1;
                minLen = Math.min(minLen, currLen);
                sum -= nums[j];
                j++;
            }
        }

        if(minLen != n + 1)
            return minLen;
        else
            return 0;
    }
}

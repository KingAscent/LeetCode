class Solution {
    public List<Integer> minSubsequence(int[] nums) {
        int n = nums.length;
        int sum = 0;
        int total = 0;
        ArrayList<Integer> ans = new ArrayList<>();
        Arrays.sort(nums);

        for(int i = 0; i < n; i++){
            total += nums[i];
        }
        
        for(int i = n - 1; 0 <= i; i--){
            ans.add(nums[i]);
            sum += nums[i];
            if(total - sum < sum)
                break;
        }

        return ans;
    }
}

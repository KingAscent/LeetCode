class Solution {
    public int pivotIndex(int[] nums) {
        int pivot = -1;
        int left = 0;
        int total = 0;

        for(int n : nums)
            total += n;
        
        for(int i = 0; i < nums.length; i++){
            if(left * 2 == total - nums[i]){
                pivot = i;
                break;
            }else{
                left += nums[i];
            }
        }

        return pivot;
    }
}

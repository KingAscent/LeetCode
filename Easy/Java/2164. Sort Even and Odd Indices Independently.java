class Solution {
    public int[] sortEvenOdd(int[] nums) {
        // Evens
        for(int i = 0; i < nums.length; i += 2){
            for(int j = i + 2; j < nums.length; j += 2){
                if(nums[j] <= nums[i]){
                    int temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp;
                }
            }
        }

        // Odds
        for(int i = 1; i < nums.length; i += 2){
            for(int j = i + 2; j < nums.length; j += 2){
                if(nums[i] <= nums[j]){
                    int temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp;
                }
            }
        }

        return nums;
    }
}

class Solution {
    public int alternatingSubarray(int[] nums) {
        int n = nums.length; 
        int alt = 0;

        /*
            Alternating pattern:
            x1 - x0 = 1
            x2 - x1 = -1
            x3 - x2 = 1
            Substitution:
            x1 - x0 = i % 2
        */
        
        for(int i = 0; i < n; i++){
            for(int j = i + 1; j < n && nums[i] + (j - i) % 2 == nums[j]; j++){
                alt = Math.max(alt, j - i + 1);
            }
        }

        return 1 < alt ? alt : -1;
    }
}

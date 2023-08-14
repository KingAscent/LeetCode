class Solution {
    public int unequalTriplets(int[] nums) {
        int count = 0;
        int n = nums.length;

        for(int i = 0; i < n - 2; i++){
            int a = nums[i];
            for(int j = i + 1; j < n - 1; j++){
                int b = nums[j];
                for(int k = i + 2; k < n; k++){
                    int c = nums[k];
                    if(i < j && j < k){
                        if(a != b && b != c && a != c)
                            count++;
                    }
                }
            }
        }

        return count;
    }
}

class Solution {
    public int minOperations(int[] nums) {
        int count = 0;
        int prev = 0;

        for(int n : nums){
            if(n <= prev){
                count += prev + 1 - n;
                prev++;
            }else{
                prev = n;
            }
        }

        return count;
    }
}

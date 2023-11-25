class Solution {
    public int maximumStrongPairXor(int[] nums) {
        int xor = 0;
        Arrays.sort(nums);

        for(int x : nums){
            for(int y : nums){
                xor = Math.abs(x - y) <= Math.min(x, y) ? Math.max(xor, x ^ y) : xor;
            }
        }

        return xor;
    }
}

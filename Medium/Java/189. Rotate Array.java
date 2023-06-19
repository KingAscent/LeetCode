class Solution {
    public void rotate(int[] nums, int k) {
        // In the event k is larger than nums.length,
        // simplify so to not rotate in circles
        int n = nums.length;
        k %= n;
        int[] temp = new int[n];
        
        for(int i = 0; i < n; i++){
            temp[(i + k) % n] = nums[i];
        }

        for(int i = 0; i < n; i++){
            nums[i] = temp[i];
        }
    }
}

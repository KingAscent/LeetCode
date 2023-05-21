class Solution {
    public int trap(int[] height) {
        int left = 0, right = height.length - 1;
        int maxLeft = height[left], maxRight = height[right];
        int count = 0;

        // Use two pointers to find out where water is trapped
        while(left < right){
            if(maxLeft < maxRight){
                left++;
                maxLeft = Math.max(maxLeft, height[left]);
                count += maxLeft - height[left];
            }else{
                right--;
                maxRight = Math.max(maxRight, height[right]);
                count += maxRight - height[right];
            }
        }

        return count;
    }
}

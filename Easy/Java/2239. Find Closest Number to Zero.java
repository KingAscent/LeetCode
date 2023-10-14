class Solution {
    public int findClosestNumber(int[] nums) {
        int num = 100001;

        for(int i : nums){
            if(Math.abs(i) < Math.abs(num) || i == Math.abs(num))
                num = i;
        }

        return num;
    }
}

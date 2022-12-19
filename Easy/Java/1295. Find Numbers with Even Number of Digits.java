class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;
        
        for(int i : nums){
            int digits = 0;
            while(0 < i){
                digits++;
                i /= 10;
            }
            if(digits % 2 == 0)
                count++;
        }

        return count;
    }
}

class Solution {
    public int averageValue(int[] nums) {
        int count = 0;
        int avg = 0;

        for(int n : nums){
            if(n % 6 == 0){
                avg += n;
                count++;
            }
        }

        return avg == 0 ? 0 : avg / count;
    }
}

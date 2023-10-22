class Solution {
    public int countEven(int num) {
        int count = 0;

        for(int i = 2; i <= num; i++){
            int temp = i;
            int sum = 0;
            while(0 < temp){
                sum += temp % 10;
                temp /= 10;
            }
            if(sum % 2 == 0)
                count++;
        }

        return count;
    }
}

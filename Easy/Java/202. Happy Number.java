class Solution {
    public boolean isHappy(int n) {
        while(n != 1 && n != 4){
            int sum = n;
            n = 0;
            while(sum != 0){
                int temp = sum % 10;
                n += temp * temp;
                sum /= 10;
            }
        }

        return n == 1;
    }
}

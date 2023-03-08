class Solution {
    public int reverse(int x) {
        boolean isNeg = false;
        int rev = 0;

        // Check if the number is negative
        if(x < 0){
            x *= -1;
            isNeg = true;
        }

        while(0 <= x){
            // Handle overflow
            if(214748364 < rev)
                return 0;
            if(10 <= x){
                int temp = x % 10;
                x /= 10;
                rev = (rev * 10) + temp;
            }else{
                rev = (rev * 10) + x;
                x = -1;
            }
        }

        if(isNeg)
            rev *= -1;
        
        return rev;
    }
}

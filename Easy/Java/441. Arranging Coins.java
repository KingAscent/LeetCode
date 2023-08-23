class Solution {
    public int arrangeCoins(int n) {
        int count = 0; 
        int row = 1;

        while(0 < n){
            n -= row;
            row++;
            if(0 <= n)
                count++;
        }

        return count;
    }
}

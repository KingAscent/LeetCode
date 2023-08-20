class Solution {
    public int totalMoney(int n) {
        int mon = n / 7; // Get number of full weeks
        int bank = 0;

        // Money from full weeks
        for(int i = 1; i <= mon; i++){
            bank += 7 * (i + 3);
        }

        // Money for leftover days
        for(int i = 7 * mon; i < n; i++){
            mon++;
            bank += mon;
        }
        
        return bank;
    }
}

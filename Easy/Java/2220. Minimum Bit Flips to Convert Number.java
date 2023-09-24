class Solution {
    public int minBitFlips(int start, int goal) {
        int xor = start ^ goal; // This will give the xor of start and goal
        int count = 0;
        
        while(xor != 0){
            if((xor & 1) == 1)
                count++;
            xor >>= 1; // Shift right
        }

        return count;
    }
}

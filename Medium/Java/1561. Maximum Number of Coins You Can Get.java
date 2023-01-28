class Solution {
    public int maxCoins(int[] piles) {
        // Sort the array, then initialize a variable to contain the max
        // number of coins you can have, and initialize a variable of piles.length
        Arrays.sort(piles);
        int max = 0;
        int len = piles.length;

        // Use a for loop to distribute the coins
        for(int i = len / 3; i < len - 1; i += 2){
            max += piles[i];
        }

        // Return the max number of coins you can have
        return max;
    }
}

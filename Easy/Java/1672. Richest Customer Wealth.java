class Solution {
    public int maximumWealth(int[][] accounts) {
        // Keep track of the richest customer
        int richest = 0;
        
        // Go over the 2-dimensional int array adding up each customer's
        // money, and then compare their money to the richest customer
        for(int i = 0; i < accounts.length; i++){
            int wealth = 0;
            for(int j = 0; j < accounts[i].length; j++){
                wealth += accounts[i][j];
            }
            if(richest < wealth){
                richest = wealth;
            }
        }
        
        // Return the richest customer's wealth
        return richest;
    }
}

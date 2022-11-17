class Solution {
    public int maxProfit(int[] prices) {
        int buy = 0;
        int sell = 1;
        int maximum = 0;

        // Use a sliding window to find the maximum
        while(sell < prices.length){
            if(prices[buy] < prices[sell]){
                int profit = prices[sell] - prices[buy];
                maximum = Math.max(maximum, profit);
            }else{
                buy = sell;
            }
            sell++;
        }

        return maximum;
    }
}

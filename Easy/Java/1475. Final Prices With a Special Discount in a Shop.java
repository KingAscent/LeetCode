class Solution {
    public int[] finalPrices(int[] prices) {
        for(int i = 0; i < prices.length; i++){
            if(i + 1 == prices.length)
                break;
            for(int j = i + 1; j < prices.length; j++){
                if(prices[j] <= prices[i]){
                    prices[i] -= prices[j];
                    break;
                }
            }
        }

        return prices;
    }
}

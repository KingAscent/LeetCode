var maxProfit = function(prices) {
    let buy = 0;
    let sell = 1;
    let maximum = 0;

    // Use a sliding window to find the maximum
    while(sell < prices.length){
        if(prices[buy] < prices[sell]){
            let profit = prices[sell] - prices[buy];
            maximum = Math.max(maximum, profit);
        }else{
            buy = sell;
        }
        sell++;
    }

    return maximum;
};

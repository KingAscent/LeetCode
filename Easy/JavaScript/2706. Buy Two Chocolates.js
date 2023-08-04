var buyChoco = function(prices, money) {
    prices.sort((a, b) => a - b);
    let price = prices[0] + prices[1];
    if(money < price)
        return money;
    else
        return money - price;
};

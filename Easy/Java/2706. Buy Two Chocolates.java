class Solution {
    public int buyChoco(int[] prices, int money) {
        Arrays.sort(prices);
        int price = prices[0] + prices[1];
        if(money < price)
            return money;
        else
            return money - price;
    }
}

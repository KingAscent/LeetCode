class Solution(object):
    def buyChoco(self, prices, money):
        prices.sort()
        price = prices[0] + prices[1]
        if money < price:
            return money
        else:
            return money - price

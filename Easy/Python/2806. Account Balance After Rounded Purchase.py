class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        n = purchaseAmount % 10
        bal = 0

        if n < 5:
            bal = purchaseAmount - n
        else:
            bal = purchaseAmount + 10 - n
        
        return 100 - bal

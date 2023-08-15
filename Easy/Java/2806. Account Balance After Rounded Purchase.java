class Solution {
    public int accountBalanceAfterPurchase(int purchaseAmount) {
        int n = purchaseAmount % 10;
        int bal = 0;

        if(n < 5)
            bal = purchaseAmount - n;
        else
            bal = purchaseAmount + 10 - n;

        return 100 - bal;
    }
}

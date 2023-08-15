var accountBalanceAfterPurchase = function(purchaseAmount) {
    let n = purchaseAmount % 10;
    let bal = 0;

    if(n < 5)
        bal = purchaseAmount - n;
    else
        bal = purchaseAmount + 10 - n;
    
    return 100 - bal;
};

var arrangeCoins = function(n) {
    let count = 0;
    let row = 1;

    while(0 < n){
        n -= row;
        row++;
        if(0 <= n)
            count++;
    }

    return count;
};

var totalMoney = function(n) {
    let mon = Math.floor(n / 7); // Get number of full weeks
    let bank = 0;

    // Money from full weeks
    for(let i = 1; i <= mon; i++){
        bank += 7 * (i + 3);
    }

    // Money for leftover days
    for(let i = 7 * mon; i < n; i++){
        mon++;
        bank += mon;
    }

    return bank;
};

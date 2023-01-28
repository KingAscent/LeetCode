var maxCoins = function(piles) {
    // Sort the array, then initialize a variable to contain the max
    // number of coins you can have, and initialize a variable of piles.length
    piles.sort((a, b) => a - b);
    let max = 0;
    const len = piles.length;

    // Use a for loop to distribute the coins
    for(let i = len / 3; i < len - 1; i += 2){
        max += piles[i];
    }

    // Return the max number of coins you can have
    return max;
};

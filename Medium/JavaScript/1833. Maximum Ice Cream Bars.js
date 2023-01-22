var maxIceCream = function(costs, coins) {
    // Counting Sort Algorithm
    // Find the max in the array
    let maximum = costs[0];
    costs.forEach((c) => {
        maximum = Math.max(c, maximum);
    });
    
    // Find the frequency of each cost
    costFreq = Array(maximum + 1).fill(0);
    costs.forEach((c) => {
        costFreq[c]++;
    })
    
    // Buy the lowest cost ice cream bars to maximize
    // the amount of ice cream bars purchased
    let count = 0;
    for(let i = 1; i <= maximum; i++){
        let freq = costFreq[i];
        if(coins < i){
            break;
        }
        let buy = Math.min(freq, Math.floor(coins / i));
        coins -= i * buy;
        count += buy;
    }

    return count;
};

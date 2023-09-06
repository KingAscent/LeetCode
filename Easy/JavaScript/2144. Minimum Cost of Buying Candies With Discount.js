var minimumCost = function(cost) {
    cost.sort((a, b) => a - b);
    let minCost = 0;
    let n = cost.length;

    for(let i = 0; i < n; i++){
        if(i % 3 != n % 3)
            minCost += cost[i];
    }

    return minCost;
};

var maxJump = function(stones) {
    let cost = stones[1];

    for(let i = 2; i < stones.length; i++){
        cost = Math.max(cost, stones[i] - stones[i - 2]);
    }

    return cost;
};

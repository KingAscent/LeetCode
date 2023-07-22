var lastStoneWeight = function(stones) {
    stones.sort((a, b) => a - b);
    let n = stones.length;
    if(n == 1)
        return stones[0];
    
    while(0 < stones[n - 2]){
        let temp = stones[n - 1] - stones[n - 2];
        stones[n - 2] = 0;
        stones[n - 1] = temp;
        stones.sort((a, b) => a - b);
    }

    return stones[n - 1];
};

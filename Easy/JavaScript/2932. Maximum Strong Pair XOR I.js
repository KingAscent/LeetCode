var maximumStrongPairXor = function(nums) {
    let xor = 0;
    nums.sort((a, b) => a - b);

    for(let x of nums){
        for(let y of nums){
            xor = Math.abs(x - y) <= Math.min(x, y) ? Math.max(xor, x ^ y) : xor;
        }
    }

    return xor;
};

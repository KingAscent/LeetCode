var minBitFlips = function(start, goal) {
    let xor = start ^ goal; // This will give us the xor of start and goal
    let count = 0;

    while(xor != 0){
        if((xor & 1) == 1)
            count++;
        xor >>= 1; // Shift right
    }

    return count;
};

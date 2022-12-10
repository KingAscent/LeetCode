var arithmeticTriplets = function(nums, diff) {
    let count = 0;
    let set = new Set();

    nums.forEach(n => {
        if(set.has(n - diff) && set.has(n - diff * 2))
            count++;
        set.add(n);
    })

    return count;
};

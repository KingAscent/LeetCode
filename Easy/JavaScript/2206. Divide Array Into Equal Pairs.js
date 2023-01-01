var divideArray = function(nums) {
    const seen = new Set();

    nums.forEach(i => {
        if(seen.has(i))
            seen.delete(i);
        else
            seen.add(i);
    })

    return seen.size == 0;
};

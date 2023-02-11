var minimumOperations = function(nums) {
    let set = new Set;

    nums.forEach(i => {
        if(0 < i)
            set.add(i);
    });

    return set.size;
};

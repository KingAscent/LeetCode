var repeatedNTimes = function(nums) {
    const appearance = new Map();
    var num = 0;

    nums.forEach(i => {
        if(appearance.has(i))
            appearance.set(i, appearance.get(i) + 1);
        else
            appearance.set(i, 1);
    })

    nums.forEach(i => {
        if(appearance.get(i) === (nums.length / 2))
            num = i;
    })

    return num;
};

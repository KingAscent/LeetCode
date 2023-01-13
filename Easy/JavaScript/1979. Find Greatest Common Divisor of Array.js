var findGCD = function(nums) {
    nums.sort((a, b) => a - b);
    let min = nums[0]
    let max = nums[nums.length - 1];
    let greatest = 0;

    for(let i = 1; i <= max; i++){
        if(max % i === 0 && min % i === 0)
            greatest = i;
    }

    return greatest;
};

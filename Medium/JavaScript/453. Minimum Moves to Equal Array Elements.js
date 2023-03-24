var minMoves = function(nums) {
    let sum = 0;
    let min = nums[0];

    for(let i = 0; i < nums.length; i++){
        if(nums[i] < min)
            min = nums[i];
        sum += nums[i];
    }

    return sum - (nums.length * min);
};

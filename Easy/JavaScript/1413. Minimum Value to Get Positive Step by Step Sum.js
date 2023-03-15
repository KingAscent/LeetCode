var minStartValue = function(nums) {
    let sum = 0;

    for(let i = 0; i < nums.length; i++){
        sum += nums[i];
        nums[i] = sum;
    }

    nums.sort((a, b) => a - b);

    if(0 < nums[0])
        return 1;
    else
        return Math.abs(nums[0]) + 1;
};

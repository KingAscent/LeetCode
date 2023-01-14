var findFinalValue = function(nums, original) {
    nums.sort((a, b) => a - b);

    for(let i = 0; i < nums.length; i++){
        if(nums[i] == original)
            original *= 2;
        else if(original < nums[i])
            break;
    }

    return original;
};

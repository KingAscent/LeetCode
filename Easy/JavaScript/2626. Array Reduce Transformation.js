var reduce = function(nums, fn, init) {
    let i = 0;

    while(i < nums.length){
        init = fn(init, nums[i]);
        i++;
    }

    return init;
};

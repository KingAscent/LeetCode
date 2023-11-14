var getMinDistance = function(nums, target, start) {
    let n = nums.length;

    for(let i = 0; i < nums.length; i++){
        if(nums[i] == target)
            n = Math.min(n, Math.abs(i - start));
    }

    return n;
};

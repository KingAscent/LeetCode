var isMonotonic = function(nums) {
    if(nums.length == 1)
        return true;
    
    let inc = true;
    let dec = true;

    for(let i = 0; i < nums.length - 1; i++){
        if(nums[i] < nums[i + 1])
            dec = false;
        if(nums[i + 1] < nums[i])
            inc = false;
        if(!inc && !dec)
            return false;
    }

    return inc || dec;
};

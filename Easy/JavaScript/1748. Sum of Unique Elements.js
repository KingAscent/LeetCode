var sumOfUnique = function(nums) {
    let map = new Map();
    let count = 0;

    for(let i = 0; i < nums.length; i++){
        if(!map[nums[i]])
            map[nums[i]] = 1;
        else
            map[nums[i]]++;
    }

    for(let i = 0; i < nums.length; i++){
        if(map[nums[i]] == 1)
            count += nums[i];
    }
    
    return count;
};

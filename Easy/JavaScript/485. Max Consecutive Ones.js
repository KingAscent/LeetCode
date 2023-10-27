var findMaxConsecutiveOnes = function(nums) {
    let count = 0;
    let track = 0;

    for(let i = 0; i < nums.length; i++){
        if(nums[i] == 1)
            track++;
        else
            track = 0;
        count = Math.max(count, track);
    }

    return count;
};

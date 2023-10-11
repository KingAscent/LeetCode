var findDisappearedNumbers = function(nums) {
    let missing = [];
    let count = Array(nums.length).fill(0);

    for(let i = 0; i < nums.length; i++)
        count[nums[i] - 1]++;
    for(let i = 0; i < nums.length; i++){
        if(count[i] == 0)
            missing.push(i + 1);
    }

    return missing;
};

var thirdMax = function(nums) {
    nums.sort((a, b) => a - b);
    let count = 0;
    let third = nums[0];

    for(let i = nums.length - 1; 0 <= i; i--){
        if(third != nums[i]){
            third = nums[i];
            count++;
        }
        if(count == 3)
            break;
    }

    return count == 3 ? third : nums[nums.length - 1];
};
